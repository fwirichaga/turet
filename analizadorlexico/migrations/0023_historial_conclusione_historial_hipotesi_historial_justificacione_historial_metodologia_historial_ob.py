# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 04:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analizadorlexico', '0022_auto_20160818_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='historial_conclusione',
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
        migrations.CreateModel(
            name='historial_hipotesi',
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
        migrations.CreateModel(
            name='historial_justificacione',
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
        migrations.CreateModel(
            name='historial_metodologia',
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
        migrations.CreateModel(
            name='historial_objetivo',
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
        migrations.CreateModel(
            name='historial_planteamiento',
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
        migrations.CreateModel(
            name='historial_pregunta',
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
