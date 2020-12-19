# Generated by Django 3.1.1 on 2020-12-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campingcar', '0027_auto_20201219_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='advanced_payment_1',
            field=models.IntegerField(default=25, help_text='1차 중도금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!'),
        ),
        migrations.AlterField(
            model_name='car',
            name='advanced_payment_2',
            field=models.IntegerField(default=25, help_text='2차 중도금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!'),
        ),
        migrations.AlterField(
            model_name='car',
            name='contract_payment',
            field=models.IntegerField(default=25, help_text='계약금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!'),
        ),
        migrations.AlterField(
            model_name='car',
            name='remaining_payment',
            field=models.IntegerField(default=25, help_text='잔금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!'),
        ),
    ]
