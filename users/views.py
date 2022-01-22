from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, filters
from users.serializers import *
from users.permissions import *


class UserView(viewsets.ModelViewSet):
    """
    Пользователь
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (OnlyAuthorized,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('id',)
    search_fields = ('id',)
