from rest_framework import serializers
from .models import User

class SetDataRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'fullname')


