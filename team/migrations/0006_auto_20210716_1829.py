# Generated by Django 3.2.4 on 2021-07-16 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_rename_zipcde_team_zipcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='team',
            name='address2',
        ),
    ]