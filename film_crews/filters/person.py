from django_filters import rest_framework as filters
from ..models.persons import Person


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PersonFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    category_id = CharFilterInFilter(field_name='category__id', lookup_expr='in')

    class Meta:
        model = Person
        fields = ('category', 'category_id')
