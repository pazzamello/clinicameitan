# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class ItemAgenda(models.Model):
	data = models.DateField()
	hora = models.TimeField()
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	usuario = models.ForeignKey(User)
	participantes = models.ManyToManyField(User,
		related_name='item_participantes')


	def __unicode__(self):
		return u"Titulo: %s Data/Hora:%s / %s" % (
		self.titulo, self.data, self.hora)


class Phone(models.Model):
    CELULAR = 'CEL'
    RESIDENCIAL = 'RES'
    COMERCIAL = 'COM'
    PHONE_TYPE_CHOICES = (
            (CELULAR, 'Celular'),
            (RESIDENCIAL, 'Residencial'),
            (COMERCIAL, 'Comercial'),
            )
    phoneType = models.CharField(max_length=3,choices=PHONE_TYPE_CHOICES, default=CELULAR)
    phoneNumber = models.CharField(max_length=20)


class Document(models.Model):
    CPF = 'CPF'
    RG = 'RG'
    CNH = 'CNH'
    DOCUMENT_TYPE_CHOICES = (
            (CPF, 'Cadastro Pessoa Física'),
            (RG, 'Carteira de Identidade'),
            (CNH, 'Carteira Nacional de Habilitação'),
            )
    documentType = models.CharField(max_length=3,choices=DOCUMENT_TYPE_CHOICES, default=CPF)
    documentNumber = models.CharField(max_length=50)

class Person(models.Model):
    firstName = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    foneticName = models.CharField(max_length=300)
    cpf = models.CharField(max_length=11, blank=True)
    street = models.CharField(max_length=500)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=50)
    district  = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    uf = models.CharField(max_length=2, null=True)
    cep = models.CharField(max_length=9, blank=True)
    birthDate = models.DateField()
    phone = models.ForeignKey(Phone, null=True)
    document = models.ForeignKey(Document, null=True)

class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    responsible = models.OneToOneField(Person, related_name='responsible', on_delete=models.SET_NULL, null=True)

class HealthProfessional(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

def envia_email(**kwargs):
	try:
		item = kwargs['instance']
	except KeyError:
		return

	for participante in item.participantes.all():
		if not participante.email:
			continue
		dados = (item.titulo, item.data, item.hora)
 	
		participante.email_user(subject="[evento] %s  dia %s as %s ",
			message="Evento: %(titulo)s\n Dia: %(data)s\n Hora: %(hora)s\n",
		from_email=item.usuario.email)

"""
models.signals.post_save.connect(envia_email, sender=ItemAgenda,
		dispatch_uid="agenda.models.ItemAgenda")
"""
