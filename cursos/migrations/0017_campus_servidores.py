# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-17 17:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cursos", "0016_cursonocampus_perfil_libras"),
    ]

    operations = [
        migrations.AddField(
            model_name="campus",
            name="servidores",
            field=models.ManyToManyField(
                to=settings.AUTH_USER_MODEL,
                verbose_name="Servidores",
                blank=True,
                related_name="lotacoes",
            ),
        ),
    ]