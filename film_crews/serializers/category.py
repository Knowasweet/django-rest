from rest_framework import serializers
from ..models.categories import Category
from django.db.models import Q


class CategorySerializer(serializers.ModelSerializer):
    """ Категория """

    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, attrs):
        super().validate(attrs)
        if type(str(self.context['request']).split('/')[::-1][1]) == int:
            name = Category.objects.filter(Q(name=attrs.get("name")),
                                           ~Q(id=str(self.context['request']).split('/')[::-1][1]))
            if name.exists():
                raise serializers.ValidationError({"error": "Данная category уже существует"})
        return attrs
