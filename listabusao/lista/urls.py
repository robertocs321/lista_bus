from django.urls import path, include

from . import views

urlpatterns = [
path('', views.listar, name='menu'),
path('cadastrar/', views.cadastrar, name='cadastrar'),
path('editar/<int:id>', views.editar, name='editar'),
path('lista/(<int:id>)', views.tirar, name='tirar'),
path('nova_lista/', views.novalista, name='novalista'),
]
