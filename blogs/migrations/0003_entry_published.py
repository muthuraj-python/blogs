# Generated by Django 3.1.5 on 2021-02-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210201_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
