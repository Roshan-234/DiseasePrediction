# Generated by Django 4.1.6 on 2023-02-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0011_alter_heartdisease_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartdisease',
            name='sex',
            field=models.IntegerField(blank=True),
        ),
    ]