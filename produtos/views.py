from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produto
from .forms import ProdutoForm, EditProdutoForm

class ProdutoCreate(LoginRequiredMixin, CreateView, ListView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'tabela_produtos.html'
    success_url = reverse_lazy('tabela_produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['txtBotao'] = 'Cadastrar'

        return context
    


class ProdutoUpdate(LoginRequiredMixin, UpdateView, ListView):
    model = Produto
    form_class = EditProdutoForm
    template_name = 'tabela_produtos.html'
    success_url = reverse_lazy('tabela_produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['txtBotao'] = 'Editar'

        return context
    

class ProdutoDelete(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'excluir_produto.html'
    success_url = reverse_lazy('tabela_produtos')