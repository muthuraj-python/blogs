# Generated by Django 3.1.5 on 2021-02-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20210202_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercomment',
            name='block',
            field=models.BooleanField(default=False),
        ),
    ]
