# Generated by Django 3.2.10 on 2021-12-23 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_usercontext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsevent',
            name='kind',
        ),
    ]
