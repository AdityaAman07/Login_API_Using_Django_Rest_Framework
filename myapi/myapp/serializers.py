from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=6, max_length=12)
    password = serializers.CharField(min_length=6)
