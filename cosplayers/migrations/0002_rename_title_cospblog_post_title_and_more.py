# Generated by Django 4.0.3 on 2022-03-31 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosplayers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cospblog',
            old_name='title',
            new_name='post_title',
        ),
        migrations.RenameField(
            model_name='cospblog',
            old_name='blogitself',
            new_name='your_post',
        ),
    ]
