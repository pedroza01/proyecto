# Generated by Django 4.2.5 on 2023-09-07 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order', models.FloatField(verbose_name='Orden de compra')),
                ('quantity_products', models.FloatField(verbose_name='Cantidad productos')),
                ('existing_products', models.FloatField(verbose_name='Productos existentes')),
                ('batches_products', models.FloatField(verbose_name='Numero lotes de productos')),
                ('expiration_date', models.DateField(verbose_name='Fecha vencimiento')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
                'db_table': 'Inventario',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('expiration_date', models.DateField(verbose_name='Fecha vencimiento')),
                ('serial_number', models.FloatField(verbose_name='Número de serie')),
                ('weight', models.FloatField(verbose_name='Gramaje')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('quantity', models.FloatField(verbose_name='Cantidad')),
                ('type_presentation', models.CharField(default='default_value', max_length=80, verbose_name='Tipo de presentación')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
                'ordering': ['id'],
            },
        ),
    ]
