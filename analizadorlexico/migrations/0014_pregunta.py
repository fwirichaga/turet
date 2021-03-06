# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-12 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analizadorlexico', '0013_justi_objetivo_planteamiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('densidad', models.DecimalField(decimal_places=2, max_digits=3)),
                ('sofisticacion', models.DecimalField(decimal_places=2, max_digits=3)),
                ('variedad', models.DecimalField(decimal_places=2, max_digits=3)),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analizadorlexico.usuario')),
            ],
        ),
    ]
