from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from alumnos.models import Alumno

def alumnos(request):
    mymembers = Alumno.objects.all().values()
    template = loader.get_template('all_alumnos.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
