# Generated by Django 3.0.8 on 2020-07-20 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200720_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='pessoa',
        ),
        migrations.AddField(
            model_name='card',
            name='pessoa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa'),
            preserve_default=False,
        ),
    ]
