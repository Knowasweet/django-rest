from rest_framework import serializers
from ..models.persons import Person


class PersonSerializer(serializers.ModelSerializer):
    """ Личность """

    title = serializers.CharField(min_length=1)
    photo = serializers.ImageField(required=True)

    class Meta:
        model = Person
        fields = '__all__'
