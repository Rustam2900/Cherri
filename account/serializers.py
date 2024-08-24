from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import User
class UserRegisterSerializer(serializers.Serializer):
    user_type = serializers.ChoiceField(choices=User.UserType)
    full_name = serializers.CharField(required=False)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(min_length=8, write_only=True)
    company_name = serializers.CharField(required=False)
    confirm_password = serializers.CharField(min_length=8, write_only=True)


    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                _('Passwords are not match')
            )
