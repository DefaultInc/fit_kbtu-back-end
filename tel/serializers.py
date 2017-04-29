from rest_framework import serializers

from tel.models import Telephone


class TelephoneCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephone
        fields = ('user_name', 'phone',)

    def create(self, validated_data):
        return Telephone.objects.create(**validated_data)


class TelephoneSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField()

    class Meta:
        model = Telephone
        fields = ('id', 'user_name', 'phone', 'created_date',)
