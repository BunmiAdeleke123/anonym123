# Generated by Django 3.0rc1 on 2020-02-01 04:24

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200131_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('attrs', django_mysql.models.JSONField(default=dict)),
            ],
        ),
    ]
