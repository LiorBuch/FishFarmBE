# Generated by Django 3.2.13 on 2022-04-28 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logi', '0011_auto_20220429_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='fishText',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logi.fish'),
        ),
        migrations.AlterField(
            model_name='tank',
            name='tankID',
            field=models.IntegerField(default=1),
        ),
    ]
