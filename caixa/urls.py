from django.urls import path
from .views import ControlarCaixa, CaixaUpdate, CaixaDelete
from . import views

urlpatterns = [
    path('controlar_caixa', ControlarCaixa.as_view(), name='controlar_caixa'),
    path('exportar_pdf', views.exportar_pdf, name='exportar_pdf'),
    path('update_caixa/<int:pk>', CaixaUpdate.as_view(), name="update_caixa"),
    path('delete_caixa/<int:pk>', CaixaDelete.as_view(), name="delete_caixa"),
]