from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, filters
from ..models.categories import Category
from film_crews.permissions import OnlyAuthorized
from film_crews.serializers.category import CategorySerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (OnlyAuthorized,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('id', 'name')
    search_fields = ('id', 'name')
