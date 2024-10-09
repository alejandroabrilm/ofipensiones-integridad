from django.shortcuts import render, redirect, get_object_or_404
from .models import Institucion
from .forms import InstitucionForm

def institucion_list(request):
    instituciones = Institucion.objects.all()
    return render(request, 'institucion_list.html', {'instituciones': instituciones})

def institucion_create(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('institucion_list')
    else:
        form = InstitucionForm()
    return render(request, 'institucion_form.html', {'form': form})

def institucion_update(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    if request.method == 'POST':
        form = InstitucionForm(request.POST, instance=institucion)
        if form.is_valid():
            form.save()
            return redirect('institucion_list')
    else:
        form = InstitucionForm(instance=institucion)
    return render(request, 'institucion_form.html', {'form': form})

def institucion_delete(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    if request.method == 'POST':
        institucion.delete()
        return redirect('institucion_list')
    return render(request, 'institucion_confirm_delete.html', {'institucion': institucion})

