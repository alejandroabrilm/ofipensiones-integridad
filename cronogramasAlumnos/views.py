from django.shortcuts import render, redirect, get_object_or_404
from .models import CronogramaAlumno
from .forms import CronogramaForm
from ofipensiones.auth0backend import getRole
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .logic.logic import get_cronograma, get_cronogramas, create_cronograma
from django.core.exceptions import PermissionDenied

# Decorador para asegurar que solo los usuarios con el rol "Gerencia" tengan acceso
@login_required
def role_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        role = getRole(request)
        if role != "Gerencia":
            raise PermissionDenied("You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Aplicar el decorador a las vistas
@login_required
@role_required
def cronograma_list(request):
    # Usar ORM de Django para obtener cronogramas
    cronogramas = get_cronogramas()
    context = {
        'cronogramas': cronogramas
    }
    return render(request, 'cronograma_list.html', context)

@login_required
@role_required
def cronograma_create(request):
    if request.method == 'POST':
        form = CronogramaForm(request.POST)
        if form.is_valid():
            create_cronograma(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created cronograma')
            return redirect('cronograma_list')  # Cambié la redirección a la lista después de crear
        else:
            print(form.errors)  # Aquí es útil pero en producción debería ser registrado o mostrado al usuario
    else:
        form = CronogramaForm()

    context = {
        'form': form,
    }
    return render(request, 'cronograma_form.html', context)

@login_required
@role_required
def cronograma_update(request, pk):
    # Usar get_object_or_404() de manera segura
    cronograma = get_object_or_404(CronogramaAlumno, pk=pk)
    if request.method == 'POST':
        form = CronogramaForm(request.POST, instance=cronograma)
        if form.is_valid():
            form.save()
            return redirect('cronograma_list')  # Redirigir a la lista después de actualizar
    else:
        form = CronogramaForm(instance=cronograma)
    return render(request, 'cronograma_form.html', {'form': form})

@login_required
@role_required
def cronograma_delete(request, pk):
    # Usar get_object_or_404() de manera segura
    cronograma = get_object_or_404(CronogramaAlumno, pk=pk)
    if request.method == 'POST':
        cronograma.delete()  # Usar el ORM para eliminar de forma segura
        return redirect('cronograma_list')  # Redirigir a la lista después de eliminar
    return render(request, 'cronograma_confirm_delete.html', {'cronograma': cronograma})


