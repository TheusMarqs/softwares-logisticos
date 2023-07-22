from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'valorCusto', 'margemCusto']

    def clean(self):
        cleaned_data = super().clean()
        valorCusto = cleaned_data.get('valorCusto')
        margemCusto = cleaned_data.get('margemCusto')

        if valorCusto is not None and margemCusto is not None:
            # Convertendo a margemCusto para uma porcentagem decimal (0.1 representa 10%)
            margemCusto = margemCusto / 100
            valorVenda = valorCusto + (valorCusto * margemCusto)
            cleaned_data['valorVenda'] = valorVenda
            self.cleaned_data['valorVenda'] = valorVenda  # Adicionando o valor calculado como atributo do formulário

        return cleaned_data
