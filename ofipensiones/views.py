from django.shortcuts import render
from alumnos.models import Alumno
from cronogramasAlumnos.models import CronogramaAlumno
from django.http import JsonResponse



def home(request):
    return render(request, 'home.html')


def healthCheck(request):
    return JsonResponse({"message": "OK"}, status=200)

def pagos_pendientes(request, alumno_id):
    # Obtener el alumno
    alumno = Alumno.objects.get(documento_identidad=alumno_id)
    
    # Consultar los pagos pendientes del cronograma
    pagos_pendientes = CronogramaAlumno.objects.filter(alumno=alumno, pagado=False)
    
    # Pasar los pagos pendientes y la información del alumno al contexto de la plantilla
    context = {
        "alumno": alumno,
        "pagos_pendientes": pagos_pendientes
    }
    
    return render(request, 'pagos_pendientes.html', context)