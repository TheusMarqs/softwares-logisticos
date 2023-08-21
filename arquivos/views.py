from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .models import Registro, Item
from django.urls import reverse_lazy
from .forms import RegistroForm, ItemForm
from django.forms import inlineformset_factory
from clientes.models import Cliente
from produtos.models import Produto
from django.http import HttpResponse
import json
from crispy_forms.utils import render_crispy_form
from django.db import transaction
from django.views import View

class RegistrarCreate(GroupRequiredMixin, CreateView):
    group_required = [u"vendedor", u"gerente"]
    model = Registro
    form_class = RegistroForm
    template_name = 'registrar.html'
    success_url = reverse_lazy('registrar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ItemFormSet = inlineformset_factory(Registro, Item, form=ItemForm, extra=4, can_delete=False)
        
        if self.request.POST:
            context['itens_formset'] = ItemFormSet(self.request.POST, instance=self.object)
        else:
            context['itens_formset'] = ItemFormSet(instance=self.object)

        registros = Registro.objects.all()
        registro_id = registros.count() + 1
        registro_format = str(registro_id).zfill(4)

        context['produtos'] = Produto.objects.all()
        context['clientes'] = Cliente.objects.all()
        context['registro_format'] = registro_format

        submitRegistro = 'Salvar'
        context['submitRegistro'] = submitRegistro

        return context

    
    def form_valid(self, form):
        context = self.get_context_data()
        itens_formset = context['itens_formset']

        if itens_formset.is_valid():
            print(itens_formset.cleaned_data)
            self.object = form.save()
            self.object.vendedor = self.request.user.username
            self.object.produto_id = self.request.POST.get('item_set-0-produto')
            self.object.save()
            itens_formset.instance = self.object
            itens_formset.save()
            print("form valido")
            return super().form_valid(form)
        else:
            print("form invalido")
            print(itens_formset.errors)
            return self.render_to_response(self.get_context_data(form=form))

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

class RegistrosList(GroupRequiredMixin, View):
    group_required = [u"vendedor", u"gerente"]

    def get(self, request):
        registros = Registro.objects.all()
        pedidos = registros.filter(tipo='P')
        orcamentos = registros.filter(tipo='O')
        return render(request, 'registros.html', {'orcamentos': orcamentos, 'pedidos': pedidos})
        

class RegistroUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u"vendedor", u"gerente"]
    model = Registro
    form_class = RegistroForm
    template_name = 'registrar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        ItemFormSet = inlineformset_factory(Registro, Item, form=ItemForm, extra=4, can_delete=False)
        
        if self.request.POST:
            context['itens_formset'] = ItemFormSet(self.request.POST, instance=self.object)
        else:
            context['itens_formset'] = ItemFormSet(instance=self.object)

        print(context['itens_formset'].management_form)
        
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        itens_formset = context['itens_formset']

        if itens_formset.is_valid():
            self.object = form.save()
            itens_formset.instance = self.object
            itens_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return self.object.get_absolute_url()