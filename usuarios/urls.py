from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import RegistrarUsuarioView

urlpatterns = [
	path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
	path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
	path('logout/', auth_views.logout_then_login, {'login_url': '/login/'}, name="logout"),
	path('editar/', views.editar, name="editar"),
	path('alterar/', views.alterar, name="alterar"),
]