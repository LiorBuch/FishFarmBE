# Generated by Django 3.2.13 on 2022-04-28 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logi', '0012_auto_20220429_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tank',
            name='fishText',
        ),
    ]
