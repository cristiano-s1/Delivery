from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products, name="products"),
    path('contato/', views.contato, name='contato'),
    path('viewCarrinho/', views.viewCarrinho, name="viewCarrinho"),
    path('enviarPedido/', views.enviarPedido, name="enviarPedido"),
    path('deleteItemCarrinho/<int:car_id>/', views.deleteItemCarrinho, name="deleteItemCarrinho"),
    path('criarPedidoUsuario/<int:user_id>/', views.criarPedidoUsuario, name="criarPedidoUsuario"),
    path('meusPedidos/<int:user_id>/', views.meusPedidos, name="meusPedidos"),
    path('addToCart/<int:prod_id>/', views.addToCart, name="addToCart")
]
