from django.shortcuts import render, redirect
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfil.models import Perfil
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required, login_required

from django.http import HttpResponse

class RegistrarUsuarioView(View):

	template_name = 'registrar.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		form = RegistrarUsuarioForm(request.POST)

		if form.is_valid():
			dados_form = form.data
			usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])

			perfil = Perfil(nome = dados_form['nome'],
						telefone = dados_form['telefone'],
						empresa = dados_form['empresa'],
						usuario = usuario)
			perfil.save()

			return redirect('index')

		return render(request, self.template_name, {'form': form})

def editar(request):
	dados_usuario = User.objects.get(id=request.user.id)
	return render(request, 'editar.html', {'dados':dados_usuario})

@login_required
@require_http_methods(['POST'])
# @permission_required
def alterar(request):
	form = RegistrarUsuarioForm(request.POST)
	if form.verifica_alteracao():
		dados_form = form.data
		usuario = User.objects.get(id=request.user.id)
		usuario.username = dados_form['nome']
		usuario.email = dados_form['email']
		usuario.set_password(dados_form['senha'])

		usuario_perfil = Perfil.objects.get(usuario=usuario)
		usuario_perfil.telefone = dados_form['telefone']
		usuario_perfil.empresa = dados_form['empresa']

		usuario_perfil.save()
		usuario.save()

		return redirect('index')

	return redirect('editar')