from rest_framework import serializers
from .models import BlogDESC, Aftor, Kategoriya


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aftor
        fields = ['id', 'full_name', 'image']

class KategoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoriya
        fields = ['id', 'name']

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    kategorya = KategoriyaSerializer()

    class Meta:
        model = BlogDESC
        fields = ['id', 'description', 'date', 'category', 'author', 'image', 'title']
