# Generated by Django 3.0.6 on 2022-12-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20200610_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published',
            field=models.DateTimeField(default='2022-12-11 15:50:27'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1024),
        ),
    ]
