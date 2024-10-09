from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'curso_list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'curso_form.html', {'form': form})

def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso_form.html', {'form': form})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')
    return render(request, 'curso_confirm_delete.html', {'curso': curso})

def curso_detail(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'curso_detail.html', {'curso': curso})

