# Generated by Django 3.0rc1 on 2020-01-31 15:52

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200131_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='People',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=1000, size=None),
        ),
    ]