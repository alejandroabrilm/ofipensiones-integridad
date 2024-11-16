from django.shortcuts import render, redirect, get_object_or_404
from .models import CronogramaAlumno
from .forms import CronogramaForm
from ofipensiones.auth0backend import getRole

def cronograma_list(request):
    cronogramas = CronogramaAlumno.objects.all()
    return render(request, 'cronograma_list.html', {'cronogramas': cronogramas})

def cronograma_create(request):
    if request.method == 'POST':
        form = CronogramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cronograma_list')
    else:
        form = CronogramaForm()
    return render(request, 'cronograma_form.html', {'form': form})

def cronograma_update(request, pk):
    cronograma = get_object_or_404(CronogramaAlumno, pk=pk)
    if request.method == 'POST':
        form = CronogramaForm(request.POST, instance=cronograma)
        if form.is_valid():
            form.save()
            return redirect('cronograma_list')
    else:
        form = CronogramaForm(instance=cronograma)
    return render(request, 'cronograma_form.html', {'form': form})

def cronograma_delete(request, pk):
    cronograma = get_object_or_404(CronogramaAlumno, pk=pk)
    if request.method == 'POST':
        cronograma.delete()
        return redirect('cronograma_list')
    return render(request, 'cronograma_confirm_delete.html', {'cronograma': cronograma})

