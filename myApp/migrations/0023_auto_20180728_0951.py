# Generated by Django 2.0.6 on 2018-07-28 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0022_auto_20180727_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'text (คำตอบยาว)'), ('short-text', 'short text (คำตอบสั้น)'), ('radio', 'choices (คำตอบแบบสเกล)')], default='text', max_length=200, verbose_name='Type'),
        ),
    ]