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

class ControlarCaixa(GroupRequiredMixin, LoginRequiredMixin, CreateView, ListView):
    group_required = [u"financeiro", u"gerente"]
    model = Transacoes
    fields = ['tipo', 'valor', 'descricao']
    template_name = 'controlar_caixa.html'
    success_url = reverse_lazy('controlar_caixa')

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