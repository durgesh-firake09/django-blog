# Generated by Django 4.0 on 2021-12-26 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_comments_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='postSno',
            new_name='post',
        ),
    ]
