from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.app_login, name='app_login'),
    path('login/', views.app_login, name='app_login'), #view app login
    path('logout/', views.app_logout, name='app_logout'), #view app login
    path('signup/', views.signup, name='app_signup'),

    path('pagina-principal/', views.pagina_principal, name='pagina_principal'),

    path('clientes/', views.index,  name='app_cliente'),
    path('cadastrar-cliente/', views.form_modelform, name='cadastrar-cliente'),
    path('delete-cliente/<int:cliente_id>/', views.delete_cliente, name='delete_cliente'),
    path('update-cliente/<int:cliente_id>/', views.update, name='update_cliente'),

    path('produtos/', views.products, name="app_produtos"),
    path('cadastrar-produto/', views.form_modelformproduto, name='cadastrarproduto'),
]

