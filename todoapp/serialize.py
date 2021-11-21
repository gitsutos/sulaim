from rest_framework import serializers
from .models import Costlist

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costlist
        fields = ['text','amount','person_used']

    def validate_content(self, value):
        return value