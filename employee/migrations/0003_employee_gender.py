# Generated by Django 2.0.5 on 2018-05-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20180521_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
