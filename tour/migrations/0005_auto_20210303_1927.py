# Generated by Django 3.1.4 on 2021-03-03 13:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='des',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]