# Generated by Django 3.1.3 on 2020-11-22 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0016_auto_20201120_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contribuição',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribuição', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Data', to='processos.data')),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo_De_Vida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo_de_vida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contribuição', to='processos.contribuição')),
            ],
        ),
    ]
