# Generated by Django 4.1.5 on 2023-01-03 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('date', models.DateField(default=datetime.date(2023, 1, 3))),
                ('buytime', models.DateTimeField()),
                ('buyprice', models.FloatField()),
                ('instrument', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('sellprice', models.FloatField()),
                ('diff', models.FloatField()),
                ('status', models.CharField(max_length=20)),
                ('profitloss', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
