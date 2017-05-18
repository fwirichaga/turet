# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analizadorlexico', '0008_auto_20160804_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='hipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('densidad', models.CharField(max_length=30)),
                ('sofisticacion', models.CharField(max_length=30)),
                ('variedad', models.CharField(max_length=30)),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analizadorlexico.usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='hipotesi',
            name='idparrafo',
        ),
        migrations.DeleteModel(
            name='hipotesi',
        ),
    ]