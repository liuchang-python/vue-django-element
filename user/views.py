import datetime
import time

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User


def mydefault(obj):
    if isinstance(obj, User):
        return {
            'id': obj.id,
            'username': obj.username,
            'password': obj.password,
            'birth': datetime.datetime.strftime(obj.birth, '%Y/%m/%d'),
            'age': obj.age,
            'address': obj.address,
        }


def users(request):
    rst = User.objects.all()

    return JsonResponse(list(rst), safe=False, json_dumps_params={'default': mydefault})


def get_user(request):
    user_id = request.GET.get('id')
    print(user_id)
    rst = User.objects.filter(pk=user_id).first()
    return JsonResponse(rst, safe=False, json_dumps_params={'default': mydefault})


def del_user(request):
    id = request.GET.get('id')
    print(id)
    rst = User.objects.filter(pk=id).first()
    if rst:
        with transaction.atomic():
            rst.delete()
        return JsonResponse({'status': 1, 'msg': '成功'})
    return JsonResponse({'status': 0, 'msg': '失败'})


def add_user(request):
    username = request.GET.get('username')
    age = request.GET.get('age')
    password = request.GET.get('password')
    address = request.GET.get('address')
    print(username, password, age, address)

    with transaction.atomic():
        User.objects.create(username=username, password=password, age=age, address=address)
        return JsonResponse({'status': 1})
    # return JsonResponse({'status': 0})


def alter_user(request):
    user_id = request.GET.get('user_id')
    username = request.GET.get('username')
    age = request.GET.get('age')
    password = request.GET.get('password')
    address = request.GET.get('address')
    print(user_id, username, password, age, address)

    rst = User.objects.filter(pk=user_id).first()
    if rst:
        with transaction.atomic():
            rst.username = username
            rst.age = age
            rst.password = password
            rst.address = address
            rst.save()
            return JsonResponse({'status': 1})
    return JsonResponse({'status': 0})


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# @method_decorator(csrf_protect, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        if user_id:
            user_obj = User.objects.filter(pk=user_id).values('id', 'birth', 'username', 'password', 'address').first()
            if user_obj:
                return JsonResponse({
                    'status': 200,
                    'message': '单用户查询成功',
                    'res': user_obj,
                })
        else:
            user_dict = User.objects.all().values('id', 'birth', 'username', 'password', 'address')
            if user_dict:
                return JsonResponse({
                    'status': 200,
                    'message': '多用户查询成功',
                    'res': list(user_dict),
                })
        return JsonResponse({
            'status': 401,
            'message': '查询用户不成功',
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = request.POST.get('age')
        address = request.POST.get('address')

        print(username, password, age, address)
        try:
            print(1)
            user_obj = User.objects.create(username=username, password=password, age=age, address=address)
            print(2)
            return JsonResponse({
                'status': 200,
                'message': '增加成功',
                'res': {'username': user_obj.username,
                        'password': user_obj.password,
                        'age': user_obj.age,
                        'address': user_obj.address,
                        },
            })
        except Exception:
            return JsonResponse({
                'status': 400,
                'message': '增加失败',
            })


class UsersAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print('GET DRF SUCCESS')
        return Response('GET OK')

    def post(self, request, *args, **kwargs):
        print('DRF POST View')
        return Response('POST OK')
