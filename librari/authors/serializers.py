from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Author, User, Book, Article, Biography
from django.contrib.auth.models import User
from rest_framework import serializers



class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserSerializerWithFullName(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
