from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.http import FileResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transacoes
from django.template.loader import render_to_string
import os
from django.conf import settings
from weasyprint import HTML
from io import BytesIO
from datetime import datetime
import locale
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.contrib.messages import constants

class ControlarCaixa(GroupRequiredMixin, LoginRequiredMixin, CreateView, ListView):
    group_required = [u"financeiro", u"gerente"]
    model = Transacoes
    fields = ['tipo', 'valor', 'descricao']
    template_name = 'controlar_caixa.html'
    success_url = reverse_lazy('controlar_caixa')

    def form_valid(self, form):
        response = super().form_valid(form)
        transacoes = Transacoes.objects.all()
        tipo_nome = ''
        for t in transacoes:
            if t.tipo == 'E':
                tipo_nome = 'Entrada'
            else:
                tipo_nome = 'Saída'
        messages.add_message(self.request, constants.SUCCESS, f'{tipo_nome} registrada com sucesso!')
        return response

    def get_queryset(self):
        txt_desc = self.request.GET.get('descricao')
        caixa = Transacoes.objects.filter(dataTrans__day = datetime.now().day)

        if txt_desc:
            caixa = caixa.filter(descricao__icontains=txt_desc)

        return caixa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['editar'] = False

        return context
    
class CaixaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView, ListView):
    group_required = [u"financeiro", u"gerente"]
    model = Transacoes
    fields = ['tipo', 'valor', 'descricao']
    template_name = 'controlar_caixa.html'
    success_url = reverse_lazy('controlar_caixa')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, constants.SUCCESS, 'Transação atualizada com sucesso!')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['editar'] = True

        return context

class CaixaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"financeiro", u"gerente"]
    model = Transacoes
    template_name = 'excluir_caixa.html'
    success_url = reverse_lazy('controlar_caixa')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, constants.SUCCESS, 'Transação removida com sucesso!')
        return response


def exportar_pdf(request):
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    transacoes = Transacoes.objects.filter(dataTrans__month = datetime.now().month)

    path_template = os.path.join(settings.BASE_DIR, 'templates/partials/extrato.html')
    template_render = render_to_string(path_template, {'transacoes': transacoes})
    mes_atual = datetime.now().strftime('%B')
    ano_atual = datetime.now().strftime('%Y')

    path_output = BytesIO()
    HTML(string=template_render).write_pdf(path_output)
    path_output.seek(0)

    nome_pdf = f"Extrato - {mes_atual} - {ano_atual}.pdf"

    return FileResponse(path_output, filename=nome_pdf)