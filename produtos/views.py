from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produto
from .forms import ProdutoForm

class ProdutoCreate(LoginRequiredMixin, CreateView, ListView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'tabela_produtos.html'
    success_url = reverse_lazy('tabela_produtos')


class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'valorCusto', 'margemCusto', 'valorVenda']
    template_name = 'tabela_produtos.html'
    success_url = reverse_lazy('tabela_produtos')

class ProdutoDelete(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'excluir_produto.html'
    success_url = reverse_lazy('tabela_produtos')