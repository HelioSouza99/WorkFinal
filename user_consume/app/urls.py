from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('', views.index, name='app_index'),
    path('', views.app_login, name='app_login'),
    path('app_index/', views.index, name='app_index'),
    path('pagina-principal/', views.pagina_principal, name='pagina_principal'),
    path('clientes/', views.index,  name='app_index'),
    # path('pedidos/', views.pedidos, name='pedidos'),
    # path('produtos/', views.produtos, name='produtos'),

    path('login/', views.app_login, name='app_login'), #view app login
    path('logout/', views.app_logout, name='app_logout'), #view app login
    path('signup/', views.signup, name='app_signup'),
    path('cadastrar-cliente/', views.form_modelform, name='cadastrar-cliente'),
    path('delete-cliente/<int:cliente_id>/', views.delete_cliente, name='delete_cliente'),
    path('update/<int:cliente_id>/', views.update, name='update_cliente'),
    path('modelform/', views.form_modelform, name ="form_modelform"),
    # path('list/<int:list_id>/', views.client_list, name='todo_list'),
]