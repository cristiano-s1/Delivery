import uuid
from django.db import models


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]  # -1 Incluindo o segundo nome para imagem
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Produto(models.Model):
    STATUS_PROD = (
        (u'ativo', u'ativo'),
        (u'inativo', u'inativo'),
    )

    nome_produto = models.CharField(max_length=50)
    codigo_produto = models.CharField(max_length=10, blank=True)
    descricao_produto = models.CharField(max_length=500, blank=True)
    preco_produto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    status_produto = models.CharField(choices=STATUS_PROD, max_length=10, default=0)

    def __str__(self):
        return self.nome_produto


class Carrinho(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    produto_id = models.IntegerField(null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_produto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)


class Pedido(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    nr_pedido = models.IntegerField(null=True, blank=True)
    produto_id = models.IntegerField(null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_produto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    status_pedido = models.CharField(max_length=15, default="Pendente")

    def __str__(self):
        return self.status_pedido


class View_Carrinho(models.Model):
    produto_id = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(default=1, primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    nome_produto = models.CharField(max_length=50)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_produto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qt_itens = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'View_Carrinho'


class View_Pedidos(models.Model):
    produto_id = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(default=1, primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    nr_pedido = models.IntegerField(null=True, blank=True)
    nome_produto = models.CharField(max_length=50)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_produto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    status_pedido = models.CharField(max_length=15, default="Pendente")

    class Meta:
        managed = False
        db_table = 'View_Pedidos'

