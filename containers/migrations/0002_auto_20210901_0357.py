# Generated by Django 3.2.6 on 2021-09-01 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='currency',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='rate',
            name='destination',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='rate',
            name='forty',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='rate',
            name='fortyhc',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='rate',
            name='twenty',
            field=models.CharField(max_length=10),
        ),
    ]
