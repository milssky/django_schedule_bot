# Generated by Django 4.0.1 on 2022-01-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_tguser_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='tg_hash',
            field=models.CharField(default='', max_length=200),
        ),
    ]
