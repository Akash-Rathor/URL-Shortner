# Generated by Django 3.2.5 on 2021-07-20 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_shorturls_delete_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturls',
            name='ShortUrl',
            field=models.URLField(db_index=True),
        ),
        migrations.AlterField(
            model_name='shorturls',
            name='delete_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 22, 51, 40, 253177)),
        ),
        migrations.AlterField(
            model_name='shorturls',
            name='url',
            field=models.URLField(db_index=True),
        ),
    ]
