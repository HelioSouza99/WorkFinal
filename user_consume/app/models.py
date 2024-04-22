from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.contrib.auth.models import User

class User(AbstractUser):
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class Cliente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo")
    maioridade = models.BooleanField(default=False, verbose_name="Maioridade")
    alergia_gluten = models.BooleanField(default=False, verbose_name="Alergia")
    veganos = models.BooleanField(default=False, verbose_name="Vegano")
    id_registro = models.AutoField(primary_key=True)

    def __str__(self):
        return "ID: {}, Nome: {}, Sexo: {}, Maioridade: {}, Alergia: {}, Vegano: {}".format(
            self.id_registro,
            self.nome, 
            self.sexo,
            self.maioridade,
            self.alergia_gluten,
            self.veganos)


