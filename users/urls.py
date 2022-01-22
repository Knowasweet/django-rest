from django.urls import path
from users.views import *

users_list = UserView.as_view({'get': 'list', 'post': 'create'})
user_detail = UserView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
urlpatterns = [
    path('', users_list, name='users'),
    path('<int:pk>/', user_detail, name='user-detail'),
]
