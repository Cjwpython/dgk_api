#coding: utf-8
from django.conf import settings
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group

from user.models import User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(help_text='密码', write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'id')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        group_enterprise, _ = Group.objects.get_or_create(name='enterprise')
        user.groups.add(group_enterprise)
        return user