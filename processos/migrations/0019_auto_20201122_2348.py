# Generated by Django 3.1.3 on 2020-11-22 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0018_auto_20201122_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciclo_de_vida',
            old_name='ciclo_de_vida',
            new_name='contribuicao',
        ),
        migrations.RenameField(
            model_name='contribuicao',
            old_name='contribuicao',
            new_name='data',
        ),
    ]
