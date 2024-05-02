from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.app_login, name='app_login'),
    path('login/', views.app_login, name='app_login'), #view app login
    path('logout/', views.app_logout, name='app_logout'), #view app login
    path('signup/', views.signup, name='app_signup'),

    path('pagina-principal/', views.pagina_principal, name='pagina_principal'),

    path('base-clientes/', views.cliente,  name='app_cliente'),
    path('cadastrar-cliente/', views.form_client, name='cadastrar-cliente'),
    path('delete-cliente/<int:cliente_id>/', views.delete_cliente, name='delete_cliente'),
    path('update-cliente/<int:cliente_id>/', views.update_cliente, name='update_cliente'),

    path('base-produtos/', views.products, name="app_produtos"),
    path('cadastrar-produto/', views.form_product, name='cadastrar-produto'),
    path('update-produto/<int:produto_id>/', views.update_product, name='update_produto'),
    path('delete-produto/<int:produto_id>/', views.delete_product, name='delete_produto'),

    path('base-pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('cadastrar-pedido/', views.form_order, name='adicionar_pedidos'),
    path('pedidos/update-pedido/<int:pedido_id>/', views.update_order, name='update_pedido'),
    path('pedidos/delete-pedido/<int:pedido_id>/', views.delete_order, name='delete_pedido'),
]

