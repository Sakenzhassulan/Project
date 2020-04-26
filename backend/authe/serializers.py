from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['email'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        return user
