from django.shortcuts import render, redirect, get_object_or_404
from .models import CronogramaAlumno
from .forms import CronogramaForm
from ofipensiones.auth0backend import getRole
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .logic.logic import get_cronograma, get_cronogramas, create_cronograma

@login_required
def cronograma_list(request):
    role = getRole(request)
    if role == "Gerencia":
        cronogramas = get_cronogramas()
        context = {
            'cronogramas': cronogramas
        }
        return render(request, 'cronograma_list.html', context)
    else:
        return HttpResponse("Unauthorized User")
    
@login_required
def cronograma_create(request):
    role = getRole(request)
    if role == "Gerencia":
        if request.method == 'POST':
            form = CronogramaForm(request.POST)
            if form.is_valid():
                create_cronograma(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created variable')
                return HttpResponseRedirect(reverse('cronogramaCreate'))
            else:
                print(form.errors)
        else:
            form = CronogramaForm()

        context = {
            'form': form,
        }
        return render(request, 'cronograma_form.html', context)
    else:
        return HttpResponse("Unauthorized User")


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

