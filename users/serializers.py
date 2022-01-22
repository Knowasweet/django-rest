from rest_framework import serializers
from users.models import User
from django.db.models import Q
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """ Пользователь """

    username = serializers.CharField(min_length=1)
    password = serializers.CharField(required=True, min_length=6)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
        )

    def validate(self, attrs):
        super().validate(attrs)
        if type(str(self.context['request']).split('/')[::-1][1]) == int:
            reg_username = User.objects.filter(Q(username=attrs.get("username")),
                                               ~Q(id=str(self.context['request']).split('/')[::-1][1]))
            if reg_username.exists():
                if not reg_username.first().is_active:
                    raise serializers.ValidationError({"error": "Данный username уже существует"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username"),
            password=validated_data.get("password"),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            is_active=False,
        )
        return user

    def update(self, instance: User, validated_data):
        super().update(instance, validated_data)
        instance.password = make_password(
            validated_data.get('password', instance.password)
        )
        instance.save()
        return instance
