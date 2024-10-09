from django.urls import path
from .views import curso_list, curso_create, curso_update, curso_delete, curso_detail

urlpatterns = [
    path('', curso_list, name='curso_list'),
    path('create/', curso_create, name='curso_create'),
    path('<int:pk>/update/', curso_update, name='curso_update'),
    path('<int:pk>/delete/', curso_delete, name='curso_delete'),
    path('cursos/<int:curso_id>/', curso_detail, name='curso_detail'),
]
