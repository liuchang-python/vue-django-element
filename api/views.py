# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Book
from api.serializer import BookModelSerializer, BookDeModelSerializer, BookModelSerializerV2


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')

        if book_id:
            book_obj = Book.objects.filter(pk=book_id).first()
            data = BookModelSerializer(book_obj).data

            return Response({
                'message': '查询单个成功',
                'results': data
            })
        else:
            books = Book.objects.all()
            data = BookModelSerializer(books, many=True).data

            return Response({
                'message': '查询多个成功',
                'results': data
            })

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BookDeModelSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        book_obj = serializer.save()

        return Response({
            'message': '新增图书成功',
            'results': BookModelSerializer(book_obj).data,
        }, status=status.HTTP_201_CREATED)


class BookAPIViewV2(APIView):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')

        if book_id:
            book_obj = Book.objects.filter(pk=book_id).first()
            data = BookModelSerializerV2(book_obj).data
            print(data)

            return Response({
                'message': '查询单个成功',
                'results': data
            })
        else:
            books = Book.objects.all()
            data = BookModelSerializerV2(books, many=True).data

            return Response({
                'message': '查询多个成功',
                'results': data
            })

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        if isinstance(data, dict) and data != {}:
            many = False
        elif isinstance(data, list) and data != []:
            many = True

        else:
            return Response({'message': '参数格式有误'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = BookDeModelSerializer(data=data, many=many)

        serializer.is_valid(raise_exception=True)
        book_obj = serializer.save()

        return Response({
            'message': '新增图书成功',
            'results': BookModelSerializer(book_obj).data,
        }, status=status.HTTP_201_CREATED)


    def delete(self,request,*args,**kwargs):
        book_id = kwargs.get('id')

        if book_id:
            ids = [book_id]
        else:
            ids = request.data.get('ids')

        response = Book.objects.filter(pk__in=ids,is_delete=False).update(is_delete=True)
        if response:
            return Response({
                'message':'删除成功'
            },status=status.HTTP_200_OK)
        return Response({
            'message':'删除失败或图书不存在'
        },status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,*args,**kwargs):
        data = request.data
        book_id = kwargs.get('id')

        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                'message':'修改的图书不存在'
            },status=status.HTTP_400_BAD_REQUEST)

        serializer = BookModelSerializerV2(data=data,instance=book_obj)
        serializer.is_valid(raise_exception=True)

        book = serializer.save()
        return Response({
            'message':'修改成功',
            'results':BookModelSerializerV2(book).data
        },status=status.HTTP_200_OK)

    def patch(self,request,*args,**kwargs):
        data = request.data
        book_id = kwargs.get('id')

        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                'message': '修改的图书不存在'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookModelSerializerV2(data=data, instance=book_obj)
        serializer.is_valid(raise_exception=True)

        book = serializer.save()
        return Response({
            'message': '修改成功',
            'results': BookModelSerializerV2(book).data
        }, status=status.HTTP_200_OK)