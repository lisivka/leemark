# Generated by Django 3.0.6 on 2020-06-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='media',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
