# Generated by Django 4.0.3 on 2022-04-21 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cosplayers', '0002_rename_title_cospblog_post_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cospblog',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]