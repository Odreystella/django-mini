# Generated by Django 2.2 on 2022-02-15 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bread',
            table='bread',
        ),
        migrations.AlterModelTable(
            name='cheese',
            table='cheeses',
        ),
        migrations.AlterModelTable(
            name='sandwich',
            table='sandwiches',
        ),
        migrations.AlterModelTable(
            name='sauce',
            table='sauces',
        ),
        migrations.AlterModelTable(
            name='topping',
            table='toppings',
        ),
    ]
