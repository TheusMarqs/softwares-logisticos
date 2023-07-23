from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'valorCusto', 'margemCusto']

class EditProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'valorCusto', 'margemCusto', 'valorVenda']
        widgets = {
            'valorVenda': forms.TextInput(attrs={'disabled': 'true'}),
        }