# Generated by Django 4.1.5 on 2023-02-02 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0004_rename_saveenquiry_contactenquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactenquiry',
            name='your_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
