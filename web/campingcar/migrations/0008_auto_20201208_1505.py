# Generated by Django 3.1.4 on 2020-12-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campingcar', '0007_auto_20201208_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
