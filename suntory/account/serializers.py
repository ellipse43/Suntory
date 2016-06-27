# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.validators import EmailValidator, MinLengthValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
            'email': {
                'required': True,
                'allow_null': False,
                'allow_blank': False,
            },
        }

    def create(self, validated_data):
        user = get_user_model().objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
