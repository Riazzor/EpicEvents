from django.contrib.auth import get_user_model
from rest_framework import serializers

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
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    sales_member = UserSerializer(read_only=True)
    sales_member_email = serializers.EmailField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        sales_member_email = validated_data.pop("sales_member_email", None)
        if sales_member_email:
            try:
                sales_member = User.objects.filter(groups__name__in=["sales"]).get(
                    email=sales_member_email
                )
                validated_data["sales_member"] = sales_member
            except User.DoesNotExist:
                raise serializers.ValidationError(
                    "Sales member with this email does not exist."
                )

        return super().create(validated_data)


class EventSerializer(serializers.ModelSerializer):
    support_member = UserSerializer(required=True)

    class Meta:
        model = Events
        fields = "__all__"
