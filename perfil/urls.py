from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('visualizar/<int:id_perfil>/', views.visualizar, name="visualizar"),
	path('visualizar/<int:id_perfil>/convidar/', views.convidar, name="convidar"),
    path('visualizar/<int:id_convite>/aceitar/', views.aceitar, name="aceitar"),
]