import re

from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from app.models import Student


class StudentSerializer(Serializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return '%s' % obj.id

    phone = serializers.CharField()
    name = serializers.CharField()
    password = serializers.CharField()

    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        return '%s%s%s' % ('http://127.0.0.1:8000/', 'media/', obj.pic)


# 正则验证
def re_res(n, num):
    pattern_name = '^[\u4E00-\u9FA5]{2,10}$'  # 用户名正则表达式
    pattern_pwd = '^\w{6,18}$'  # 密码正则表达式
    pattern_phone = '^1[35678]\d{9}$'  # 电话正则表达式
    if num == 'name':
        result = re.findall(pattern_name, n)
        if result:
            return True
    elif num == 'pwd':
        result = re.findall(pattern_pwd, n)
        if result:
            return True
    elif num == 'phone':
        result = re.findall(pattern_phone, n)
        if result:
            return True


class StudentDeSerializer(Serializer):
    name = serializers.CharField(
        max_length=8,
        min_length=2,
        error_messages={
            "max_length": "名字长度太长了",
            "min_length": "名字长度太短了",
        }
    )
    password = serializers.CharField()
    phone = serializers.CharField()

    re_pwd = serializers.CharField()

    # 对姓名做校验
    def validate_name(self, value):
        print('name')
        stu_obj = Student.objects.filter(name=value).first()
        if not re_res(value, 'name') or stu_obj:
            print('name1')
            raise serializers.ValidationError('用户名不合法')
        print('name2')
        return value

    # # 对电话号做校验
    # def validate_phone(self, value):
    #     print('phone')
    #     stu_obj = Student.objects.filter(phone=value).first()
    #     if not re_res(value, 'phone') or stu_obj:
    #         raise serializers.ValidationError('电话不合法')
    #     return value

    def validate(self, attrs):
        print('pwd')
        password = attrs.get('password')
        re_pwd = attrs.pop('re_pwd')
        if password != re_pwd or not re_res(password, 'pwd'):
            raise serializers.ValidationError('密码不合法')
        return attrs

    def create(self, validated_data):
        return Student.objects.create(**validated_data)


class StudentModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'password', 'gender', 'phone', 'stu_pic']

        extra_kwargs = {
            # 're_pwd': {
            #     'write_only': True
            # },
        }


    def validate(self, attrs):
        print(attrs)
        password = attrs.get('password')
        # re_pwd = attrs.pop('re_pwd')
        # if password != re_pwd or not re_res(password, 'pwd'):
        if not re_res(password, 'pwd'):
            raise serializers.ValidationError('密码不合法')
        return attrs

    def validate_name(self, value):
        print('name')
        stu_obj = Student.objects.filter(name=value).first()
        if not re_res(value, 'name') or stu_obj:
            print('name1')
            raise serializers.ValidationError('用户名不合法')
        print('name2')
        return value
