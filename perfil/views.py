from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from perfil.models import Perfil, Convite

@login_required
def index(request):
	# return HttpResponse("Bem-vindo ao ConnectedIn")
	return render(request,"index.html", {"perfis": Perfil.objects.all(), "perfil_logado": get_perfil_logado(request)})

@login_required
def visualizar(request, id_perfil):
	perfil = Perfil.objects.get(id=id_perfil)
	perfil_logado = get_perfil_logado(request)
	ja_eh_contato = perfil in perfil_logado.contatos.all() or perfil.id == perfil_logado.id
	return render(request,"visualizar.html", {"perfil":perfil,'ja_eh_contato':ja_eh_contato})

@login_required
def convidar(request, id_perfil):
	perfil_a_convidar = Perfil.objects.get(id=id_perfil)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')

@login_required
def get_perfil_logado(request):
	return request.user.perfil

@login_required
def aceitar(request, id_convite):
	convite = Convite.objects.get(id=id_convite)
	convite.aceitar()
	return redirect('index')