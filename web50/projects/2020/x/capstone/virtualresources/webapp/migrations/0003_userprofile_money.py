# Generated by Django 3.1 on 2020-08-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200812_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='money',
            field=models.IntegerField(default=1000),
        ),
    ]
