# Generated by Django 3.0.5 on 2020-06-03 08:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200421_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_visit',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 8, 58, 41, 566758, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
