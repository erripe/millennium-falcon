# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('papel', models.CharField(max_length=255)),
                ('entrada_leds', models.DateField()),
                ('saida_leds', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_projeto', models.CharField(max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('fomento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestao.Pessoa')),
                ('periodo', models.IntegerField()),
                ('status_bolsa', models.BooleanField(default=False)),
                ('valor_bolsa', models.BooleanField(default=False)),
            ],
            bases=('gestao.pessoa',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestao.Pessoa')),
                ('email', models.CharField(max_length=255)),
            ],
            bases=('gestao.pessoa',),
        ),
        migrations.CreateModel(
            name='Representante_parceiro',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestao.Pessoa')),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
            ],
            bases=('gestao.pessoa',),
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestao.Pessoa')),
                ('email', models.CharField(max_length=255)),
            ],
            bases=('gestao.pessoa',),
        ),
    ]