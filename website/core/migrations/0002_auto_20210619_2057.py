# Generated by Django 3.2.4 on 2021-06-20 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='ISBN',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre del libro'),
        ),
    ]
