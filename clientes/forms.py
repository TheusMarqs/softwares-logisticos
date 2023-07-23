from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, HTML, Button, ButtonHolder
from crispy_forms.bootstrap import FormActions
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'email', 'rg', 'cidade', 'telefone', 'numero', 'rua', 'bairro']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize o layout dos campos usando Crispy Forms
        self.helper = FormHelper()
        self.helper.form_class = 'form'
        self.helper.layout = Layout(
            Div(
                Div(css_class='col-md-1'),
                Div(Field('nome', css_class='form-control'), css_class='col-md-5'),
                Div(Field('cpf', css_class='form-control'), css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div(css_class='col-md-1'),
                Div(Field('email', css_class='form-control'), css_class='col-md-5'),
                Div(Field('rg', css_class='form-control'), css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div(css_class='col-md-1'),
                Div(Field('cidade', css_class='form-control'), css_class='col-md-5'),
                Div(Field('telefone', css_class='form-control'), css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div(css_class='col-md-1'),
                Div(Field('numero', css_class='form-control'), css_class='col-md-5'),
                Div(Field('rua', css_class='form-control'), css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div(css_class='col-md-1'),
                Div(Field('bairro', css_class='form-control'), css_class='col-md-5'),
                Div(Submit('submit', '{{ submitCliente }}', css_class='btn btn-success submit-cliente'), css_class='col-md-2 mt-4 ms-lg-4 ms-md-3 ms-xl-5'),
                Div(HTML("{% if submitCliente == 'Editar' %}<a href='{% url 'cadastrar_cliente' %}'><button class='btn btn-secondary voltar' type='button'>Voltar</button></a>{% endif %}"), css_class='col-md-2 mt-4 ms-lg-5 ms-md-5'),
                    
                css_class='row'
            ),
            
        )