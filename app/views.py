from django.db import transaction
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Student
from app.serializer import StudentSerializer, StudentDeSerializer, StudentModelSerializer


class StuAPIView(APIView):
    def get(self, request, *args, **kwargs):
        stu_id = kwargs.get('id')
        print(stu_id)
        if stu_id:
            stu_obj = Student.objects.get(pk=stu_id)
            serializer = StudentSerializer(stu_obj).data
            return Response({
                'message': '查询单个对象成功',
                "result": serializer
            })
        else:
            stu_obj = Student.objects.all()
            serializer = StudentSerializer(stu_obj, many=True).data

            return Response({
                'message': '查询所有对象成功',
                "result": serializer
            })

    def post(self, request, *args, **kwargs):
        request_data = request.data
        print(request_data)

        if not isinstance(request_data, dict) or request_data == {}:
            return Response({"message": "请求参数有误"}, status=400)

        serializer = StudentDeSerializer(data=request_data)

        if serializer.is_valid():
            stu_obj = serializer.save()
            return Response({
                'message': '创建学生成功',
                'results': StudentSerializer(stu_obj).data,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        print(user_id)
        stu_obj = Student.objects.get(pk=user_id)
        if stu_obj:
            with transaction.atomic():
                stu_obj.delete()
                return Response({
                    'message': '删除成功',
                    'result': StudentSerializer(stu_obj).data
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': '删除失败',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        stu_obj = Student.objects.get(pk=user_id)


class StuAPIViewV2(APIView):
    def get(self, request, *args, **kwargs):
        stu_id = kwargs.get('id')
        print(stu_id)
        if stu_id:
            stu_obj = Student.objects.get(pk=stu_id)
            serializer = StudentModelSerializer(stu_obj).data
            return Response({
                'message': '查询单个对象成功',
                "result": serializer
            })
        else:
            stu_obj = Student.objects.all()
            serializer = StudentModelSerializer(stu_obj, many=True).data

            return Response({
                'message': '查询所有对象成功',
                "result": serializer
            })

    def post(self, request, *args, **kwargs):
        request_data = request.data
        print(request_data)

        if not isinstance(request_data, dict) or request_data == {}:
            return Response({"message": "请求参数有误"}, status=400)

        serializer = StudentModelSerializer(data=request_data)

        if serializer.is_valid():
            stu_obj = serializer.save()
            return Response({
                'message': '创建学生成功',
                'results': StudentModelSerializer(stu_obj).data,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        print(user_id)
        stu_obj = Student.objects.get(pk=user_id)
        if stu_obj:
            with transaction.atomic():
                stu_obj.delete()
                return Response({
                    'message': '删除成功',
                    'result': StudentModelSerializer(stu_obj).data
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': '删除失败',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        data = request.data
        user_id = kwargs.get('id')
        try:
            stu_obj = Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return Response({
                'message': '修改的图书不存在'
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentModelSerializer(data=data, instance=stu_obj)
        serializer.is_valid(raise_exception=True)
        stu = serializer.save()
        return Response({
            'message': '修改成功',
            'results': StudentModelSerializer(stu).data
        }, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        data = request.data
        stu_id = kwargs.get('id')
        try:
            stu_obj = Student.objects.get(pk=stu_id)
        except Student.DoesNotExist:
            return Response({
                'message': '修改的图书不存在'
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentModelSerializer(data=data, instance=stu_obj)
        serializer.is_valid(raise_exception=True)
        stu = serializer.save()
        return Response({
            'message': '修改成功',
            'results': StudentModelSerializer(stu).data
        }, status=status.HTTP_200_OK)
