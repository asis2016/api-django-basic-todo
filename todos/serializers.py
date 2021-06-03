"""
    todos/serializers.py
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """ Serializing Todo model. """
    class Meta:
        model = Todo
        fields = ('id','title','body','created_at','updated_at')


class UserSerializer(serializers.ModelSerializer):
    """ Serializing User model. """
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
