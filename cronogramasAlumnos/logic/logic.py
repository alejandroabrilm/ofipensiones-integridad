from ..models import CronogramaAlumno

def get_cronogramas():
    queryset = CronogramaAlumno.objects.all()
    return (queryset)

def get_cronograma(id):
    cronograma = CronogramaAlumno.objects.raw("SELECT * FROM cronograma_cronograma WHERE id=%s" % id)[0]
    return (cronograma)

def create_cronograma(form):
    cronograma = form.save()
    cronograma.save()
    return ()