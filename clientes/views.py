from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#CREATE VIEW
class ClienteCreate(LoginRequiredMixin, CreateView, ListView):
    model = Cliente
    fields = ['nome', 'cpf', 'email', 'rg', 'cidade', 'telefone', 'numero', 'rua', 'bairro']
    template_name = 'cadastrar_cliente.html'
    success_url = reverse_lazy('cadastrar_cliente')

#UPDATE VIEW
class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nome', 'cpf', 'email', 'rg', 'cidade', 'telefone', 'numero', 'rua', 'bairro']
    template_name = 'cadastrar_cliente.html'
    success_url = reverse_lazy('cadastrar_cliente')

#DELETE VIEW
class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'excluir_cliente.html'
    success_url = reverse_lazy('cadastrar_cliente')
