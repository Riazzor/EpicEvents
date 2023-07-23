from rest_framework import serializers

from .models import Contract, Customer, Events


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        depth = 1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["sales_member"] = data["sales_member"]["email"]
        return data


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1

    # TODO : get from id
    # serializers for sales and support
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        depth = 1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["support_member"] = data["support_member"]["email"]
        return data
