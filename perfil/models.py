from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
	nome = models.CharField(max_length=128)
	empresa = models.CharField(max_length=128)
	telefone = models.CharField(max_length=20)
	contatos = models.ManyToManyField('self')
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")

	@property
	def email(self):
		return self.usuario.email

	def convidar(self, perfil_convidado):
		Convite(solicitante=self, convidado = perfil_convidado).save()

class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE,related_name="convites_feito")
	convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE,related_name="convites_recebidos")

	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()