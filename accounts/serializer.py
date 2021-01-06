from user.models import User
from rest_framework import serializers


class Accounts_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

