
# Create your models here.
from django.db import models

class Aluno(models.Model):
	IDA = 1
	IDAEVOLTA = 2
	VOLTA = 3
	STATUS_CHOICES = (
	    (IDA, 'Ida'),
	    (IDAEVOLTA, 'Ida e volta'),
	    (VOLTA, 'Volta'),
	    
	)


	CADASTRADO = 1
	CARONA = 2
	STATUS_CHOICES2 = (
	    (CADASTRADO, 'Cadastrado'),
	    (CARONA, 'Carona'),
	    
	)
	data = models.DateTimeField(auto_now_add=True) #default = timezone.now
	nome = models.CharField(max_length = 100)
	acao = models.IntegerField(choices=STATUS_CHOICES, default=IDAEVOLTA)
	instituicao = models.CharField(max_length = 10)
	situacao = models.IntegerField(choices=STATUS_CHOICES2, default=CADASTRADO)


	def __str__(self):
		return self.nome
