# Generated by Django 4.1.5 on 2023-02-01 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0003_saveenquiry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='saveEnquiry',
            new_name='contactEnquiry',
        ),
    ]
