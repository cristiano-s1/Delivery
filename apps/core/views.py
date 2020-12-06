from django.db.models import Sum
from django.shortcuts import render, redirect
from apps.produtos.models import Produto, Carrinho, View_Carrinho, Pedido
from apps.produtos.functions import getViewCarrinho, deletarItemCarrinho, deleteCarrinhoUser, getViewPedidos, getQuantidadeProduto


def index(request):
    return render(request, 'core/index.html')


def products(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'core/products.html', context)


def contato(request):
    return render(request, "core/contact.html")


def addToCart(request, prod_id):
    user_id = request.user.id
    produto = Produto.objects.get(id=prod_id)
    quantidade = getQuantidadeProduto(request, prod_id, user_id)
    if quantidade == 1:
        carrinho = Carrinho()
    else:
        carrinho = Carrinho.objects.get(produto_id=prod_id, user_id=user_id)
    carrinho.user_id = user_id
    carrinho.produto_id = prod_id
    carrinho.quantidade = quantidade
    carrinho.valor_unitario = produto.preco_produto
    carrinho.total_produto = produto.preco_produto * quantidade
    carrinho.save()
    mensagem = "produto -> " + produto.nome_produto + "   foi adicionado ao carrinho com sucesso!"
    produtos = Produto.objects.all().order_by("nome_produto")
    context = {
        'produtos': produtos,
        'mensagem': mensagem,
    }
    return render(request, "core/products.html", context)


def viewCarrinho(request):
    user_id = request.user.id
    viewCarrinho = getViewCarrinho(request, user_id)
    context = {
        'viewCarrinho': viewCarrinho,
        'user_id': user_id,
    }
    return render(request, "core/carrinho.html", context)


def enviarPedido(request):
    user_id = request.user.id
    viewCarrinho = getViewCarrinho(request, user_id)
    valor_total = View_Carrinho.objects.filter(user_id=user_id).aggregate(Sum('total_produto')).get('total_produto__sum', 0.00)
    if viewCarrinho:
        mensagem = ""
        context = {
            'viewCarrinho': viewCarrinho,
            'user_id': user_id,
            'valor_total': valor_total,
        }
    else:
        mensagem = "Não existe pedidos no carrinho!"
        context = {
            'user_id': user_id,
            'mensagem': mensagem,
        }
    return render(request, "core/enviarPedido.html", context)


def deleteItemCarrinho(request, car_id):
    user_id = request.user.id
    remove = deletarItemCarrinho(request, car_id)
    viewCarrinho = getViewCarrinho(request, user_id)
    valor_tortal = View_Carrinho.objects.filter(user_id=user_id).aggregate(Sum('total_produto')).get('total_produto__sum', 0.00)
    context = {
        'viewCarrinho': viewCarrinho,
        'valor_tota': valor_tortal
    }
    return render(request, "core/enviarPedido.html", context)


def criarPedidoUsuario(request, user_id):
    carrinho = getViewCarrinho(request, user_id)
    for car in carrinho:
        pedido = Pedido()
        pedido.nr_pedido = 1
        pedido.user_id = car['user_id']
        pedido.produto_id = car['produto_id']
        pedido.quantidade = car['quantidade']
        pedido.valor_unitario = car['valor_unitario']
        pedido.total_produto = car['total_produto']
        pedido.status_pedido = "Pendente"
        pedido.save()
    limparCarrinho = deleteCarrinhoUser(request, user_id)
    return redirect('/pizzaria/')


def meusPedidos(request, user_id):
    viewPedidos = getViewPedidos(request, user_id)
    valor_total = Pedido.objects.filter(user_id=user_id).aggregate(Sum('total_produto')).get('total_produto__sum', 0.00)
    context = {
        'viewPedidos': viewPedidos,
        'valor_total': valor_total
    }
    return render(request, "core/meusPedidos.html", context)



