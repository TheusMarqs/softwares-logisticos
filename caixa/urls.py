from django.urls import path
from .views import ControlarCaixa
from . import views

urlpatterns = [
    path('controlar_caixa', ControlarCaixa.as_view(), name='controlar_caixa'),
    path('exportar_pdf', views.exportar_pdf, name='exportar_pdf'),
]