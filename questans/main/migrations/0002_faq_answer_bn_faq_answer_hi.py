# Generated by Django 5.1.5 on 2025-02-01 09:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_bn',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_hi',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
