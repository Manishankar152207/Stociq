# Generated by Django 4.1.5 on 2023-01-22 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_clientlog_ip_alter_client_createdon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientlog',
            name='logout',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
