from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pago
from .forms import PagoForm

class PagoListView(ListView):
    model = Pago
    template_name = 'pago_list.html'

class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pago_form.html'
    success_url = reverse_lazy('pago_list')

class PagoUpdateView(UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pago_form.html'
    success_url = reverse_lazy('pago_list')

class PagoDeleteView(DeleteView):
    model = Pago
    template_name = 'pago_confirm_delete.html'
    success_url = reverse_lazy('pago_list')

