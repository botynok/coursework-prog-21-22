# Generated by Django 3.2.10 on 2021-12-22 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_sportevent_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sportevent',
            old_name='name',
            new_name='title',
        ),
    ]