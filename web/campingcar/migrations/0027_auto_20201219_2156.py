# Generated by Django 3.1.1 on 2020-12-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campingcar', '0026_auto_20201219_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='advanced_payment_1',
            field=models.IntegerField(default=0, help_text='1차 중도금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!'),
        ),
        migrations.AddField(
            model_name='car',
            name='advanced_payment_2',
            field=models.IntegerField(default=0, help_text='2차 중도금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!'),
        ),
        migrations.AddField(
            model_name='car',
            name='contract_payment',
            field=models.IntegerField(default=0, help_text='계약금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!'),
        ),
        migrations.AddField(
            model_name='car',
            name='remaining_payment',
            field=models.IntegerField(default=0, help_text='잔금의 비율(퍼센트)를 입력하세요. *숫자만 입력 가능!'),
        ),
        migrations.AlterField(
            model_name='company',
            name='car',
            field=models.ManyToManyField(blank=True, help_text='제작사가 만드는 차량들을 선택하세요. ', to='campingcar.Car'),
        ),
        migrations.AlterField(
            model_name='option',
            name='car',
            field=models.ManyToManyField(blank=True, help_text='옵션이 적용가능한 차량들을 선택하세요. ', to='campingcar.Car'),
        ),
    ]
