# Generated by Django 3.2.13 on 2022-04-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logi', '0010_auto_20220429_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='numberOfDecorations',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tank',
            name='numberOfFish',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tank',
            name='tankID',
            field=models.IntegerField(default=0),
        ),
    ]