# Generated by Django 4.2.2 on 2023-08-22 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0008_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appUser.profileimage', verbose_name='Profil Resmi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appUser.profileimage', verbose_name='Profil Resmi'),
        ),
    ]
