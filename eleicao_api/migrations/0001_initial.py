# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-20 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant_vagas', models.FloatField(verbose_name='quantidade')),
            ],
        ),
        migrations.CreateModel(
            name='Eleitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
            ],
        ),
        migrations.CreateModel(
            name='Secretario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='cpf')),
            ],
        ),
        migrations.AddField(
            model_name='eleicao',
            name='candidato',
            field=models.ManyToManyField(to='eleicao_api.Eleitor', verbose_name='candidato'),
        ),
        migrations.AddField(
            model_name='eleicao',
            name='secretario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secretario', to='eleicao_api.Secretario'),
        ),
    ]
