# Generated by Django 3.1.5 on 2021-01-09 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SaveBase', '0008_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='IDuser',
        ),
    ]
