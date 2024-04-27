from django import forms
from .models import Cliente, Product

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        # exclude = ("id_registro")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # Para incluir todos os campos do modelo
        # Ou especifique os campos manualmente:
        # fields = ['productname', 'description', 'price', 'available', 'category', 'ingredients', 'image', 'discount', 'rating', 'preparation_time', 'calories']