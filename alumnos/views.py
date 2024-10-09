from django.shortcuts import render, redirect, get_object_or_404

from alumnos.forms import AlumnoForm
from alumnos.models import Alumno
from cronogramasAlumnos.models import CronogramaAlumno

def alumno_list(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno_list.html', {'alumnos': alumnos})

def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm()
    return render(request, 'alumno_form.html', {'form': form})

def alumno_update(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumno_form.html', {'form': form})

def alumno_delete(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumno_list')
    return render(request, 'alumno_confirm_delete.html', {'alumno': alumno})

def alumno_detail(request, alumno_id):
    alumno = get_object_or_404(Alumno, documentoIdentidad=alumno_id)
    return render(request, 'alumno_detail.html', {'alumno': alumno})

def pagos_pendientes(request, alumno_id):
    # Obtener el alumno
    alumno = Alumno.objects.get(documentoIdentidad=alumno_id)
    
    # Consultar los pagos pendientes del cronograma
    pagos_pendientes = CronogramaAlumno.objects.filter(alumno=alumno, pagado=False)
    
    # Pasar los pagos pendientes y la información del alumno al contexto de la plantilla
    context = {
        "alumno": alumno,
        "pagos_pendientes": pagos_pendientes
    }
    
    return render(request, 'pagos_pendientes.html', context)
