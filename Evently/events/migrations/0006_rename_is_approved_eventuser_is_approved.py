# Generated by Django 5.1.6 on 2025-03-05 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_eventuser_is_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventuser',
            old_name='is_Approved',
            new_name='is_approved',
        ),
    ]
