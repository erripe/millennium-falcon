# Generated by Django 2.0.2 on 2018-03-08 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('duracao', models.CharField(max_length=255)),
                ('sobre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Fomento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=255)),
                ('detalhes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('sobre', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='parceiro',
            name='projeto',
            field=models.ManyToManyField(to='produtos.Projeto'),
        ),
        migrations.AddField(
            model_name='fomento',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Projeto'),
        ),
    ]
