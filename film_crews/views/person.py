from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework import viewsets, filters
from ..models.persons import Person

from film_crews.serializers.person import PersonSerializer
from film_crews.filters.person import PersonFilter
from drf_yasg.utils import swagger_auto_schema
from film_crews.permissions import OnlyAuthorized


@swagger_auto_schema(request_body=PersonSerializer)
class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (OnlyAuthorized,)
    filter_class = PersonFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('pk', 'title')
    search_fields = ('id', 'title')
    parser_classes = (MultiPartParser,)
