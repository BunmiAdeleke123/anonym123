# Generated by Django 3.0rc1 on 2020-01-31 15:49

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200131_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='People',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=66, size=6),
        ),
    ]