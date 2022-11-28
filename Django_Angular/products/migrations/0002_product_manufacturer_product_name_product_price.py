# Generated by Django 4.1.3 on 2022-11-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=-1000),
            preserve_default=False,
        ),
    ]