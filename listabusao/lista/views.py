from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from datetime import date
from django.utils import timezone
from django.db.models import Count
from django.http import HttpResponse
from datetime import datetime, timedelta
# Create your views here.
def listar (request):
	lista0 = Aluno.objects.all().filter(situacao=Aluno.CADASTRADO, acao=Aluno.VOLTA)
	lista1 = Aluno.objects.all().filter(situacao=Aluno.CADASTRADO, acao=Aluno.IDA)

	lista2 = Aluno.objects.all().filter(situacao=Aluno.CARONA,acao=Aluno.VOLTA)
	lista3 = Aluno.objects.all().filter(situacao=Aluno.CARONA,acao=Aluno.IDA)


	return render (request, 'main.html', {"cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})	

def tirar(request, id):
	aux2=id
	try:
		aux = Aluno.objects.get(id=id)
		aux.delete()
		return redirect('menu')
	except :
		return redirect('menu')


def novalista(request):
	data_e_hora_atuais = datetime.now()
	hora = data_e_hora_atuais.strftime('%H')#o %H retorna apenas a hora
	hora1=int(hora)
	try:
		if hora1 == 19:	
			aux = Aluno.objects.all()
			aux.delete()
			return redirect('menu')
	except :
		return redirect('menu')
	lista0 = Aluno.objects.all().filter(situacao=Aluno.CADASTRADO, acao=Aluno.VOLTA)
	lista1 = Aluno.objects.all().filter(situacao=Aluno.CADASTRADO, acao=Aluno.IDA)

	lista2 = Aluno.objects.all().filter(situacao=Aluno.CARONA,acao=Aluno.VOLTA)
	lista3 = Aluno.objects.all().filter(situacao=Aluno.CARONA,acao=Aluno.IDA)
	return render(request, 'main.html',{'alerta2':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
	

def editar(request, id):
	aux = Aluno.objects.get(id=id)
	if request.method=="POST":
		form = AlunoForm(request.POST, instance=aux)
		if form.is_valid():
			aux.save()
			return redirect('menu')
	
	form = AlunoForm(instance=aux)
	return render(request, 'editar.html', {'form':form})

def cadastrar(request):
	if request.method =='POST':
		#formularioReclamacao = Reclamacao(request.POST)
		#if formularioReclamacao.is_valid():
		
		#if nome == 'admin':
		#    return render(request, 'aluno/login.html', {'alerta3': 'Erro'})
		data_atual = date.today()
		data_e_hora_atuais = datetime.now()
		hora = data_e_hora_atuais.strftime('%H')#o %H retorna apenas a hora
		hora1=int(hora)
		if 11 <= hora1 < 20:
			lista0 = Aluno.objects.all().filter(situacao=Aluno.CADASTRADO, acao=Aluno.VOLTA)
			lista1 = Aluno.objects.all().filter(situacao=Aluno.CADASTRADO, acao=Aluno.IDA)

			lista2 = Aluno.objects.all().filter(situacao=Aluno.CARONA,acao=Aluno.VOLTA)
			lista3 = Aluno.objects.all().filter(situacao=Aluno.CARONA,acao=Aluno.IDA)
			return render(request, 'main.html',{'alerta':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
			

		nome = request.POST['nome']
		acao = request.POST['acao']
		instituicao = request.POST['instituicao']
		situacao = request.POST['situacao']

		if acao=='2':
			Aluno.objects.create(nome=nome, acao='1', instituicao=instituicao, situacao=situacao)
			Aluno.objects.create(nome=nome, acao='3', instituicao=instituicao, situacao=situacao)
			return redirect('menu')
			
		Aluno.objects.create(nome=nome, acao=acao, instituicao=instituicao, situacao=situacao)

		return redirect('menu')
	

def cadastrar1(request):
	if request.method=="POST":
		form = AlunoForm(request.POST)
		if form.is_valid():
			
			model = form.save(commit=False)
			model.save()
			
			lista = Aluno.objects.all()
			return render(request, 'main.html', {"todos": lista})

	else:
		form = AlunoForm()
	return render(request, 'main.html', {'form':form})