# Generated by Django 3.0.5 on 2020-04-20 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200420_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='api_group',
            new_name='group',
        ),
    ]
