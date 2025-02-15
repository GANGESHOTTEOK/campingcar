# Generated by Django 3.1.1 on 2020-12-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campingcar', '0028_auto_20201219_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.IntegerField(default=0, help_text='소비세의 비율(퍼센트)을 입력하세요. *숫자만 입력 가능!')),
                ('education', models.IntegerField(default=0, help_text='교육세의 비율(퍼센트)을 입력하세요. *숫자만 입력 가능!')),
                ('vat', models.IntegerField(default=0, help_text='부가가치세의 비율(퍼센트)을 입력하세요. *숫자만 입력 가능!')),
                ('registration', models.IntegerField(default=0, help_text='취등록세의 비율(퍼센트)을 입력하세요. *숫자만 입력 가능!')),
            ],
        ),
    ]
