from django.urls import path
from film_crews.views.person import PersonView

persons_list = PersonView.as_view({'get': 'list', 'post': 'create'})
person_detail = PersonView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

urlpatterns = [
    path('', persons_list, name='persons'),
    path('<int:pk>/', person_detail, name='person-detail'),
]