# Generated by Django 3.2.13 on 2022-04-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logi', '0002_auto_20220424_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='tank',
            name='gravel',
            field=models.CharField(default='https://i.imgur.com/XpQnuUx.png', max_length=1000),
        ),
        migrations.AddField(
            model_name='tank',
            name='wallpaper',
            field=models.CharField(default='https://i.imgur.com/z73rdIL.png', max_length=1000),
        ),
    ]
