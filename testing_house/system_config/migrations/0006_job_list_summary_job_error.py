# Generated by Django 2.1 on 2019-09-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0005_auto_20190907_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_list_summary',
            name='job_error',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
