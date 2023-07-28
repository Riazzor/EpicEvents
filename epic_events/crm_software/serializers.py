from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Contract, Customer, Events

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class ContractSerializer(serializers.ModelSerializer):
    sales_member = UserSerializer(required=True)

    class Meta:
        model = Contract
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    sales_member = UserSerializer(required=True)

    class Meta:
        model = Customer
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    support_member = UserSerializer(required=True)

    class Meta:
        model = Events
        fields = '__all__'
