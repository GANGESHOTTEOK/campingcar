# Generated by Django 3.1.1 on 2020-12-14 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campingcar', '0022_auto_20201211_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='option_type',
            new_name='type',
        ),
    ]
