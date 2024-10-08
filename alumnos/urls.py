from django.urls import path
from .views import pagos_pendientes

urlpatterns = [
    path('alumno/<str:alumno_id>/pagos-pendientes/', pagos_pendientes, name='pagos_pendientes'),
]