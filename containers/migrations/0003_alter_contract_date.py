# Generated by Django 3.2.6 on 2021-09-01 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0002_auto_20210901_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
