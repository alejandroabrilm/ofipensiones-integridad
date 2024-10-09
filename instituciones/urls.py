from django.urls import path
from .views import institucion_list, institucion_create, institucion_update, institucion_delete

urlpatterns = [
    path('', institucion_list, name='institucion_list'),
    path('create/', institucion_create, name='institucion_create'),
    path('<int:pk>/update/', institucion_update, name='institucion_update'),
    path('<int:pk>/delete/', institucion_delete, name='institucion_delete'),
]
