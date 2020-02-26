from rest_framework import serializers
from .models import Message
from django.utils import timezone


class MessageSerializer(serializers.ModelSerializer):
    date_posted = serializers.DateTimeField(default=timezone.now())
    author = serializers.CharField(default='unknown')


    class Meta:
        model = Message
        fields = ['id', 'author', 'email', 'content', 'date_posted']

