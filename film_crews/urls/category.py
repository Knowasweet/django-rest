from django.urls import path
from ..views.category import CategoryView

categories_list = CategoryView.as_view({'get': 'list', 'post': 'create'})
category_detail = CategoryView.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

urlpatterns = [
    path('', categories_list, name='categories'),
    path('<int:pk>/', category_detail, name='category-detail'),
]
