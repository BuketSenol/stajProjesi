# Generated by Django 4.2.2 on 2023-08-29 13:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0014_alter_profile_loginuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Yorum'),
        ),
    ]
