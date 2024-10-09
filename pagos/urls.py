from django.urls import path
from .views import PagoListView, PagoCreateView, PagoUpdateView, PagoDeleteView

urlpatterns = [
    path('', PagoListView.as_view(), name='pago_list'),
    path('create/', PagoCreateView.as_view(), name='pago_create'),
    path('update/<int:pk>/', PagoUpdateView.as_view(), name='pago_update'),
    path('delete/<int:pk>/', PagoDeleteView.as_view(), name='pago_delete'),
]
