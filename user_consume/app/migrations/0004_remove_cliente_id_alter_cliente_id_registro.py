# Generated by Django 4.2.11 on 2024-04-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cliente_alergia_gluten_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id_registro',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]