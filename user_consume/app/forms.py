from django import forms
from .models import Cliente


SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outros'),
)

BOOL = (
    ("S", "SIM"),
    ("N", "NÃO"),
)

class MeuFormulario(forms.Form):
    nome = forms.CharField(max_length=100)
    sexo = forms.ChoiceField(choices=SEXO_CHOICES)
    maioridade = forms.ChoiceField(choices=BOOL)
    alergia_gluten = forms.ChoiceField(choices=BOOL)
    veganos = forms.ChoiceField(choices=BOOL)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        # exclude = ("id_registro")

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"
        # exclude = ("id_registro")