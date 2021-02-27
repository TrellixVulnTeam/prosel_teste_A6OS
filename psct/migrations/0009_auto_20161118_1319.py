# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-18 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("psct", "0008_auto_20161116_1347"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comprovanteinscricao",
            name="chave",
            field=models.CharField(max_length=255, unique=True, verbose_name="Hash"),
        ),
        migrations.AlterField(
            model_name="comprovanteinscricao",
            name="inscricao",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comprovante",
                to="psct.Inscricao",
                verbose_name="Inscrição",
            ),
        ),
    ]