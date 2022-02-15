# Generated by Django 2.2 on 2022-02-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0002_auto_20220215_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bread',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='cheese',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='sauce',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
