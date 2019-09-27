from django.urls import path, include

from . import views

urlpatterns = [
path('menu/', views.listar, name='menu'),
path('menu/cadastrar/', views.cadastrar, name='cadastrar'),
path('editar/<int:id>', views.editar, name='editar'),
path('lista/(<int:id>)', views.tirar, name='tirar'),

]
