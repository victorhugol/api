# Generated by Django 3.0.8 on 2020-07-20 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200720_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='idCard',
        ),
        migrations.AddField(
            model_name='card',
            name='data',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
