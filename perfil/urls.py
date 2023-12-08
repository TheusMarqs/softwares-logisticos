from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('home/', views.home, name='home'),
    path('meu_perfil', views.meu_perfil, name='meu_perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('alterar_senha/', auth_views.PasswordChangeView.as_view(template_name='alterar_senha.html', success_url=reverse_lazy('senha_alterada')), name='alterar_senha'),
    path('senha_alterada/', auth_views.PasswordChangeDoneView.as_view(template_name='senha_alterada.html'), name='senha_alterada'),
]