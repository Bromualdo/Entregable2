# Generated by Django 4.1.2 on 2022-10-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entregable2', '0002_remove_familiares_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiares',
            name='nac',
            field=models.DateField(null=True),
        ),
    ]
