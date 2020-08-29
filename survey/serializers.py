from .models import Form
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    forms = serializers.PrimaryKeyRelatedField(many=True, queryset=Form.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'forms']


class FormSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Form
        fields = '__all__'