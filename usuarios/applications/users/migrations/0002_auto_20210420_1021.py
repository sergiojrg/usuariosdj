# Generated by Django 3.2 on 2021-04-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellidos',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]