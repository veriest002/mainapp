# Generated by Django 2.0.6 on 2018-07-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_auto_20180718_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('คำตอบยาว', 'คำตอบยาว'), ('คำตอบสั้น', 'คำตอบสั้น')], default='คำตอบยาว', max_length=200, verbose_name='Type'),
        ),
    ]
