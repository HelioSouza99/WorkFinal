from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from .models import CustomUserCreationForm
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from .forms import ClienteForm, ProductForm, OrdersForm
from .models import Cliente, Product, Orders
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
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
            return redirect('pagina_principal')
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
            
    return render(request, 'app/login.html')

@login_required
def app_logout(request):
    logout(request)
    return redirect('app_login')

def not_found(request, exception):
    return app_logout(request)

def pagina_principal(request):
    return render(request, 'app/pagina_principal.html')

@login_required
def cliente(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes,
        'user': request.user  # Passa o usuário autenticado para o template
    }
    return render(request, 'app/app_cliente.html', context)

def form_client(request):
    if request.method == "GET":
        form_cliente = ClienteForm()
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
    return render(request, 'app/formulario_cliente.html', context=context)

def update_cliente(request, cliente_id):
    clientes = Cliente.objects.all()  #Todos  # Move a atribuição para fora do bloco `elif`
    if request.method == "GET":
        cliente = Cliente.objects.filter(id_registro=cliente_id).first() #! cliente filtrado
        form = ClienteForm(instance=cliente)
        context = {
            'form': form,
            'clientes': clientes,
        }
        return render(request, 'app/formulario_cliente.html', context=context)
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
            return render(request, 'app/formulario_cliente.html', context=context)
        
def delete_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id_registro=cliente_id)
    cliente.delete()
    return redirect('app_cliente')


@login_required
def products(request):
    produtos = Product.objects.all()

    context = {'produtos': produtos,
             'user': request.user
             }

    return render(request, 'app/app_produtos.html', context)

def form_product(request):
    if request.method == "GET":
        form_produto = ProductForm()

    else:  # Método POST
        form_produto = ProductForm(request.POST)
        if form_produto.is_valid():
            produto = form_produto.save(commit=False)  # Evita salvar imediatamente para configurar id_registro
            produto.save()  # Salva o cliente e gera o id_registro automaticamente
            # form_produto.save()
            form_produto = ProductForm()

    produtos = Product.objects.all()
    context = {
        'form_produto': form_produto,
        'produtos': produtos
    }
    return render(request, 'app/formulario_prod.html', context=context)

def delete_product(request, produto_id):
    produto = Product.objects.get(id_registro=produto_id)
    produto.delete()
    return redirect('app_produtos')

def update_product(request, produto_id):
    produtos = Product.objects.all()  #Todos  # Move a atribuição para fora do bloco `elif`
    if request.method == "GET":
        produto = Product.objects.filter(id_registro=produto_id).first() #!produto filtrado
        form_produto = ProductForm(instance=produto)
        context = {
            'form_produto': form_produto,
            'produtos': produtos,
        }
        return render(request, 'app/formulario_prod.html', context=context)
    elif request.method == "POST":
        produto = Product.objects.filter(id_registro=produto_id).first()
        form_produto = ProductForm(request.POST, instance=produto)
        if form_produto.is_valid():
            produto = form_produto.save()
            return redirect('update_produto', produto_id=produto_id)
        else:
            context = {
                'form_produto': form_produto,
                'produtos': produtos,
            }
            return render(request, 'app/formulario_prod.html', context=context)

@login_required
def listar_pedidos(request):
    produtos = Product.objects.all()
    ordens = Orders.objects.all()
    context = {
        'ordens': ordens,
        'produtos': produtos,
    }
    return render(request, 'app/app_pedidos.html', context=context)


def form_order(request):
    if request.method == "GET":
        form_pedidos = OrdersForm()
    else:  # Método POST
        form_pedidos = OrdersForm(request.POST)
        if form_pedidos.is_valid():
            ordem = form_pedidos.save(commit=False)  # Evita salvar imediatamente para configurar id_registro
            ordem.save()  # Salva o cliente e gera o id_registro automaticamente
            form_pedidos.save()
            form_pedidos = OrdersForm()

    ordens = Orders.objects.all()
    context = {
        'form_pedidos': form_pedidos,
        'ordens': ordens
    }
    return render(request, 'app/formulario_orders.html', context=context)

def delete_order(request, pedido_id):
    ordem = Orders.objects.get(id=pedido_id)
    ordem.delete()
    return redirect('listar_pedidos')

def update_order(request,pedido_id):
    ordens = Orders.objects.all()  #Todos  # Move a atribuição para fora do bloco `elif`
    if request.method == "GET":
        ordem = Orders.objects.filter(id=pedido_id).first() #!pedido acessado pelo ID
        form_pedidos = OrdersForm(instance=ordem)
        context = {
            'form_pedidos': form_pedidos,
            'ordens': ordens,
        }
        return render(request, 'app/formulario_orders.html', context=context)
    elif request.method == "POST":
        ordem = Orders.objects.filter(id=pedido_id).first()
        form_pedidos = OrdersForm(request.POST, instance=ordem)
        if form_pedidos.is_valid():
            ordem = form_pedidos.save()
            return redirect('update_pedido', pedido_id=pedido_id)
        else:
            context = {
                'form_pedidos': form_pedidos,
                'ordens': ordens,
            }
            return render(request, 'app/formulario_orders.html', context=context)
