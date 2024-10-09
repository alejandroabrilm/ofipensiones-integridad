from django.urls import path
from .views import alumno_create, alumno_delete, alumno_list, alumno_update, pagos_pendientes, alumno_detail

urlpatterns = [
    path('', alumno_list, name='alumno_list'),
    path('create/', alumno_create, name='alumno_create'),
    path('<int:pk>/update/', alumno_update, name='alumno_update'),
    path('<int:pk>/delete/', alumno_delete, name='alumno_delete'),
    path('alumnos/<int:alumno_id>/', alumno_detail, name='alumno_detail'),
    #path('', alumno_detail, name='alumno_detail'),
    path('alumno/<str:alumno_id>/pagos-pendientes/', pagos_pendientes, name='pagos_pendientes'),
]