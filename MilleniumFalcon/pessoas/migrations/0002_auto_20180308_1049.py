# Generated by Django 2.0.2 on 2018-03-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jedi',
            name='nivel',
            field=models.CharField(choices=[('YL', 'Young ling'), ('PW', 'Padawan'), ('JD', 'Jedi'), ('MJ', 'Mestre Jedi')], default='YL', max_length=2),
        ),
        migrations.DeleteModel(
            name='Nivel',
        ),
    ]
