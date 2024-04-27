from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from .models import CustomUserCreationForm
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from .forms import ClienteForm, ProductForm
from .models import Cliente, Product
from django.urls import reverse_lazy

# Create your views here.
@login_required
def index(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes,
        'user': request.user  # Passa o usuário autenticado para o template
    }
    return render(request, 'app/app_index.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def app_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app_index')
    return render(request, 'app/login.html')

@login_required
def app_logout(request):
    logout(request)
    return redirect('app_login')

def form_modelform(request):
    if request.method == "GET":
        form = ClienteForm()
    else: # Método POST
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)  # Evita salvar imediatamente para configurar id_registro
            cliente.save()  # Salva o cliente e gera o id_registro automaticamente
            # form.save()
            form = ClienteForm()
    
    clientes = Cliente.objects.all()
    context = {
        'form': form,
        'clientes': clientes
    }
    return render(request, 'app/formulario_modelform.html', context=context)

def update(request, cliente_id):
    clientes = Cliente.objects.all()  #Todos  # Move a atribuição para fora do bloco `elif`
    if request.method == "GET":
        cliente = Cliente.objects.filter(id_registro=cliente_id).first() #! cliente filtrado
        form = ClienteForm(instance=cliente)
        context = {
            'form': form,
            'clientes': clientes,
        }
        return render(request, 'app/formulario_modelform.html', context=context)
    elif request.method == "POST":
        cliente = Cliente.objects.filter(id_registro=cliente_id).first()
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            return redirect('update_cliente', cliente_id=cliente_id)
        else:
            context = {
                'form': form,
                'clientes': clientes,
            }
            return render(request, 'app/formulario_modelform.html', context=context)
        
def delete_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id_registro=cliente_id)
    cliente.delete()
    return redirect('app_index')

def products(request):
    produtos20 = Product.objects.all()
    return render(request, 'app/produtos.html', context={'produtos20': produtos20})



def form_modelformproduto(request):
    if request.method == "GET":
        form2 = ProductForm()

    else:  # Método POST
        form2 = ProductForm(request.POST)
        if form2.is_valid():
            produto20 = form2.save(commit=False)  # Evita salvar imediatamente para configurar id_registro
            produto20.save()  # Salva o cliente e gera o id_registro automaticamente
            form2.save()
            form2 = ProductForm()

    produtos20 = Product.objects.all()
    context = {
        'form2': form2,
        'produtos20': produtos20
    }
    return render(request, 'app/formulario_modelformprod.html', context=context)
