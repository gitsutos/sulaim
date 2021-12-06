from rest_framework import serializers
from .models import Costlist


class CostlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costlist
        fields = '__all__'
