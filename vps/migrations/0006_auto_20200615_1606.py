# Generated by Django 2.2.5 on 2020-06-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0005_auto_20200615_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='cpu',
            field=models.CharField(default=1, max_length=128, verbose_name='CPU'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='ipv4',
            field=models.CharField(default=1, max_length=128, verbose_name='IPV4'),
        ),
    ]