# Generated by Django 2.2.9 on 2020-12-06 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='View_Carrinho',
            fields=[
                ('produto_id', models.IntegerField(blank=True, null=True)),
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('nome_produto', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('valor_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('qt_itens', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'View_Carrinho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='View_Pedidos',
            fields=[
                ('produto_id', models.IntegerField(blank=True, null=True)),
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('nr_pedido', models.IntegerField(blank=True, null=True)),
                ('nome_produto', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('valor_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('status_pedido', models.CharField(default='Pendente', max_length=15)),
            ],
            options={
                'db_table': 'View_Pedidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('produto_id', models.IntegerField(blank=True, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('valor_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('nr_pedido', models.IntegerField(blank=True, null=True)),
                ('produto_id', models.IntegerField(blank=True, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('valor_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('status_pedido', models.CharField(default='Pendente', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=50)),
                ('codigo_produto', models.CharField(blank=True, max_length=10)),
                ('descricao_produto', models.CharField(blank=True, max_length=500)),
                ('preco_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('status_produto', models.CharField(choices=[('ativo', 'ativo'), ('inativo', 'inativo')], default=0, max_length=10)),
            ],
        ),
    ]
