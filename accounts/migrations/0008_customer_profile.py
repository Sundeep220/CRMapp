# Generated by Django 3.1.14 on 2022-10-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20221023_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
