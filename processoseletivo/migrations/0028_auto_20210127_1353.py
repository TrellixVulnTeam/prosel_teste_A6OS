# Generated by Django 2.2.14 on 2021-01-27 13:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processoseletivo', '0027_merge_20210119_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processoseletivo',
            name='descricao',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Descrição'),
        ),
    ]