from django.urls import path
from .views import cronograma_list, cronograma_create, cronograma_update, cronograma_delete

urlpatterns = [
    path('', cronograma_list, name='cronograma_list'),
    path('create/', cronograma_create, name='cronograma_create'),
    path('<int:pk>/update/', cronograma_update, name='cronograma_update'),
    path('<int:pk>/delete/', cronograma_delete, name='cronograma_delete'),
]
