from rest_framework import serializers
from .models import SignIn

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignIn
        fields = ['email_id', 'password','department_id','aadhaar_number']