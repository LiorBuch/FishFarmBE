# Generated by Django 3.2.13 on 2022-04-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tank',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tank',
            name='size',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='userfiles',
            name='number_of_tanks',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userfiles',
            name='xp_points',
            field=models.IntegerField(default=0),
        ),
    ]