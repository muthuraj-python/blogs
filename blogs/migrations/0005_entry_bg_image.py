# Generated by Django 3.1.5 on 2021-02-02 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_usercomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='bg_image',
            field=models.ImageField(default='', upload_to='blogs'),
            preserve_default=False,
        ),
    ]
