# Generated by Django 2.1.7 on 2019-03-24 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='context',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
