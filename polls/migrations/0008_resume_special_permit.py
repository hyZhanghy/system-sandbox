# Generated by Django 3.1.5 on 2021-02-04 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210204_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='special_permit',
            field=models.BooleanField(default=False, verbose_name='是否打回修改'),
        ),
    ]
