# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-14 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("psct", "0005_auto_20161011_1700"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="email",
            options={
                "permissions": (("send_mail", "Administrador Pode Enviar Email"),),
                "verbose_name": "Email",
                "verbose_name_plural": "Emails",
            },
        ),
    ]