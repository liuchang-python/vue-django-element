from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Book, Press, Author


class PressModelSerializer(ModelSerializer):
    class Meta:
        model = Press
        fields = ('id', 'press_name', 'address')


# class AuthorModelSerializer(ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ('id', 'author_name')


class BookModelSerializer(ModelSerializer):
    press = PressModelSerializer()

    class Meta:
        model = Book
        fields = (
            'id', 'book_name', 'price', 'pic', 'press', "press_name", "press_address", 'create_time', 'author_list')
        # fields = "__all__"
        # exclude = ('is_delete','status','create_time')
        # depth = 1


class BookDeModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_name', 'price', 'authors', 'press')

        extra_kwargs = {
            'book_name': {
                'min_length': 4,
                'max_length': 8,
                'required': True,
                'error_messages': {
                    'max_length': '字段不能超过8字符'
                }
            },
            'price': {
                'max_digits': 5,
                'decimal_places': 2,
            }
        }

        def validate(self, attrs):
            return attrs

        def validate_book_name(self, value):
            book = Book.objects.filter(book_name=value).first()

            if book:
                raise serializers.ValidationError('图书名已存在')
            return value


class BookModelSerializerV2(ModelSerializer):
    class Meta:
        model = Book
        fields = ['create_time','id','book_name', 'price', 'press', 'authors','book_pic', 'pic']

        extra_kwargs = {
            'press': {
                'write_only': True
            },
            'authors': {
                'write_only': True
            },
            'pic': {
                'read_only': True
            },
            'id': {
                'read_only': True
            },
            'create_time': {
                'read_only': True
            },
        }

    def validate_pic(self, value):
        return '%s%s%s' % ('http://127.0.0.1:8000/', 'media/', value)

    def validate(self, attrs):
        return attrs

