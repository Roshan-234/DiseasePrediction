# Generated by Django 4.1.5 on 2023-02-03 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0007_alter_contactenquiry_your_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='messages',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contactenquiry',
            name='your_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]