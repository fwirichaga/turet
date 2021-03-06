# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analizadorlexico', '0015_conclusione_metodologia'),
    ]

    operations = [
        migrations.CreateModel(
            name='total_avance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hipotesis', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('justificacion', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('objetivo', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('planteamiento', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('preguntas', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('metodologia', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('conclusion', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analizadorlexico.usuario')),
            ],
        ),
    ]
