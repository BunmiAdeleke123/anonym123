# Generated by Django 3.0rc1 on 2020-04-02 12:59

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Message',
        ),
        migrations.AddField(
            model_name='profile',
            name='attrs',
            field=django_mysql.models.JSONField(default=dict),
        ),
    ]