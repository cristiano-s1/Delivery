from django.db import models, connection
from apps.produtos.models import Carrinho, View_Carrinho, View_Pedidos


def deleteProduto(self, prod_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM produtos_produto where id = %s", [prod_id])
        row = cursor.fetchone()
    return row


def deletarItemCarrinho(self, car_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM produtos_carrinho where id = %s", [car_id])
        row = cursor.fetchone()
    return row


def deleteCarrinhoUser(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM produtos_carrinho where user_id = %s", [user_id])
        row = cursor.fetchone()
    return row


def getQuantidadeProduto(self, prod_id, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(1) cont FROM produtos_carrinho where produto_id = %s and user_id = %s", [prod_id, user_id])
        row = dictfetchall(cursor)
        if row[0]['cont'] == 0:
            quantidade = 1
        else:
            cursor.execute("SELECT (quantidade + 1) quantidade FROM produtos_carrinho where produto_id = %s", [prod_id])
            row = dictfetchall(cursor)
            quantidade = row[0]['quantidade']

        class Meta:
            model = Carrinho
            fields = ['quantidade']
        return quantidade


def getViewCarrinho(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM View_Carrinho where user_id = %s order by id", [user_id])
        row = dictfetchall(cursor)

        class Meta:
            model = View_Carrinho
            fields = ['id', 'user_id', 'produto_id', 'nome_produto', 'quantidade', 'valor_unitario', 'total_produto', 'qt_itens']
    return row


def getViewPedidos(self, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM View_Pedidos where user_id = %s order by id", [user_id])
        row = dictfetchall(cursor)

        class Meta:
            model = View_Pedidos
            fields = ['id', 'nr_pedido', 'user_id', 'produto_id', 'nome_produto', 'quantidade', 'valor_unitario', 'total_produto', 'status_pedido']
    return row


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
