# Generated by Django 2.2.7 on 2020-06-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0011_auto_20200617_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='need_monitor',
            field=models.BooleanField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='是否需要监控'),
        ),
    ]