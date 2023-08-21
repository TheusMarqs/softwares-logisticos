from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produto
from .forms import ProdutoForm, EditProdutoForm
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.contrib.messages import constants


class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView, ListView):
    group_required = u"gerente"
    model = Produto
    form_class = ProdutoForm
    template_name = 'tabela_produtos.html'
    success_url = reverse_lazy('tabela_produtos')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, constants.SUCCESS, 'Produto cadastrado com sucesso!')
        return response

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')
        produtos = Produto.objects.all()

        if txt_nome:
            produtos = produtos.filter(nome__icontains=txt_nome)

        return produtos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['txtBotao'] = 'Cadastrar'

        return context


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView, ListView):
    group_required = u"gerente"
    model = Produto
    form_class = EditProdutoForm
    template_name = 'tabela_produtos.html'
    success_url = reverse_lazy('tabela_produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['txtBotao'] = 'Editar'

        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, constants.SUCCESS, 'Produto atualizado com sucesso!')
        return response
    

class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"gerente"
    model = Produto
    template_name = 'excluir_produto.html'
    success_url = reverse_lazy('tabela_produtos')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, constants.SUCCESS, 'Produto removido com sucesso!')
        return response