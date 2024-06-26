# Generated by Django 4.2.11 on 2024-04-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='alergia_gluten',
            field=models.BooleanField(default=False, verbose_name='Alergia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='maioridade',
            field=models.BooleanField(default=False, verbose_name='Maioridade'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='veganos',
            field=models.BooleanField(default=False, verbose_name='Vegano'),
        ),
    ]
