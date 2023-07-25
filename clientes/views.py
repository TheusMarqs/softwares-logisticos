from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ClienteForm
from braces.views import GroupRequiredMixin

#CREATE VIEW
class ClienteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView, ListView):
    group_required = [u"vendedor", u"gerente"]
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastrar_cliente.html'
    success_url = reverse_lazy('cadastrar_cliente')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        submitCliente = 'Cadastrar'
        context['submitCliente'] = submitCliente
        return context

#UPDATE VIEW
class ClienteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView, ListView):
    group_required = [u"vendedor", u"gerente"]
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastrar_cliente.html'
    success_url = reverse_lazy('cadastrar_cliente')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        submitCliente = 'Editar'
        context['submitCliente'] = submitCliente
        return context

#DELETE VIEW
class ClienteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"vendedor", u"gerente"]
    model = Cliente
    template_name = 'excluir_cliente.html'
    success_url = reverse_lazy('cadastrar_cliente')
