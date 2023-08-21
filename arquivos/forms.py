from django import forms
from .models import Registro, Item
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, HTML, Button, ButtonHolder
from crispy_forms.bootstrap import FormActions

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['cliente','totalPedido', 'tipo', 'vendedor', 'nome', 'cpf', 'email', 'rg', 'cidade', 'telefone', 'numero', 'rua', 'bairro', 'data']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize o layout dos campos usando Crispy Forms
        self.helper = FormHelper()
        self.helper.form_class = 'form'
        self.helper.layout = Layout(
            HTML(
                '''
                    <div class="container-fluid">
                        <div class="col-sm-9 col-md-8 m-auto">
                            {% csrf_token %}
                            <select class="form-select no-focus" id="id_cliente" name="cliente" onchange="update_cliente_data()">
                                    <option value="" data-cliente='{"nome": "", "cpf": "", "email": "", "rg": "", "cidade": "", "telefone": "", "numero": "", "rua": "", "bairro": ""}'>Selecione um cliente...</option>
                                    {% for cliente in clientes %}
                                        <option id="opcao{{cliente.id}}" value="{{ cliente.id }}" data-cliente='{"nome": "{{ cliente.nome | title }}", "cpf": "{{ cliente.cpf }}", "email": "{{ cliente.email }}", "rg": "{{ cliente.rg }}", "cidade": "{{ cliente.cidade | title }}", "telefone": "{{ cliente.telefone }}", "numero": "{{ cliente.numero }}", "rua": "{{ cliente.rua | title }}", "bairro": "{{ cliente.bairro | title }}"}'>{{ cliente.nome | title }}</option>
                                    {% endfor %}
                            </select>
                '''
            ),
            Div(
                Div(Field('tipo', css_class='form-control no-focus'), css_class='col-md-5'),
                Div(css_class='col-md-2'),
                Div(HTML("<h4>N° {{ registro_format }}</h4>"), css_class='col-md-5 mt-4'),
                css_class='row'
            ),
            Div(
                Div(Field('nome', css_class='form-control no-focus', autocomplete='off'), css_class='col-md-5'),
                Div(css_class='col-md-2'),
                Div(Field('cpf', css_class='form-control no-focus', autocomplete='off'), css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div(Field('email', css_class='form-control no-focus'), css_class='col-md-5'),
                Div(css_class='col-md-2'),
                Div(Field('rg', css_class='form-control no-focus', autocomplete='off'), css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div(HTML("<label>Vendedor</label><input class='form-control' type='text' disabled value='{{ request.user | title }}'>"), css_class='col-md-5'),
                Div(css_class='col-md-2'),
                Div(Field('data', css_class='form-control no-focus'), css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div(Field('cidade', css_class='form-control no-focus', autocomplete='off'), css_class='col-md-5'),
                Div(css_class='col-md-2'),
                Div(Field('telefone', css_class='form-control no-focus', autocomplete='off'), css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div(Field('numero', css_class='form-control no-focus', autocomplete='off'), css_class='col-md-5'),
                Div(css_class='col-md-2'),
                Div(Field('rua', css_class='form-control no-focus', autocomplete='off'), css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div(Field('bairro', css_class='form-control no-focus', autocomplete='off'), css_class='col-md-5'),
                css_class='row'
            ),
            HTML('''
                        
                    </div>
                    <hr style="margin-bottom: 10px; margin-top: 20px;">
                </div>
            
<div class="p-5">
                {{ itens_formset.management_form }}
                
    {% for formset_form in itens_formset %}
        <div class="inline-formset-item">
            <div class="row no-gutters">
                <div class="col-md-4 p-0 m-0">
                    {% if forloop.first %}
                        <h5 class="mb-4 ms-2">Produto</h5>
                    {% endif %}
                    <select name="{{ formset_form.prefix }}-produto" id="id_produto" class="form-control select custom-select no-focus" onchange="update_produto_data(this, '{{ forloop.counter0 }}'); calculateTotal(this);">

                
                        <option value="" data-produto='{"valor": ""}'>Selecione um produto...</option>
                        {% for produto in produtos %}
                            <option id="opcaoProd{{produto.id}}" value="{{ produto.id }}" data-produto='{"valor": "{{ produto.valorVenda }}"}'>{{ produto.nome | title }}</option>
                        {% endfor %}
                    
                    </select>
                </div>
                <div class="col-md-2 p-0 m-0">
                    {% if forloop.first %}
                        <h5 class="mb-4 ms-2">Quantidade</h5>
                    {% endif %}
                    <input id="id_{{ formset_form.prefix }}-quantidade" type="number" step="any" class="form-control no-focus" name="{{ formset_form.prefix }}-quantidade" placeholder="Quantidade" autocomplete="off" onchange="calculateTotal(this);">
                </div>
                <div class="col-md-2 p-0 m-0">
                    {% if forloop.first %}
                        <h5 class="mb-4 ms-2">Tamanho</h5>
                    {% endif %}
                    <input id="id_{{ formset_form.prefix }}-tamanho" type="text" class="form-control no-focus" name="{{ formset_form.prefix }}-tamanho" placeholder="Tamanho" autocomplete="off" onchange="calculateTotal(this)" onblur="formatarNumero(this)">
                </div>
                <div class="col-md-2 p-0 m-0">
                    {% if forloop.first %}
                        <h5 class="mb-4 ms-2">Valor por metro</h5>
                    {% endif %}
                    <input id="id_{{ formset_form.prefix }}-valorProd" type="number" step="any" class="form-control no-focus" name="{{ formset_form.prefix }}-valorProd" placeholder="Valor por metro" autocomplete="off" onchange="calculateTotal(this)">
                </div>
                <div class="col-md-2 p-0 m-0">
                    {% if forloop.first %}
                        <h5 class="mb-4 ms-2">Total</h5>
                    {% endif %}
                    <input id="id_{{ formset_form.prefix }}-totalProd" type="number" step="any" class="form-control no-focus" name="{{ formset_form.prefix }}-totalProd" placeholder="Total" autocomplete="off">

                </div>
            </div>
        </div>
    {% endfor %}

    <button class="btn btn-success mt-2 mb-5" type="submit" style="width: 110px;">Salvar</button>
      {% if editar %}
    <a href="{% url 'registrar' %}">
        <button class="btn btn-secondary mt-2 mb-5 ms-2" type="button">Voltar</button>
    </a>
    {% else %}
    <a href="#" target="_blank">
        <button class="btn btn-secondary mt-2 mb-5 ms-2" type="button">Exportar PDF</button>
    </a>
    {% endif %}
    <div class="col-md-4">
        <input type="number" name="totalPedido" id="id_totalPedido" step="any" class="form-control no-focus" autocomplete="off" placeholder="Total do pedido">
    </div>
</div>
            '''))
        

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['produto','quantidade', 'tamanho','valorProd', 'totalProd']