# Generated by Django 2.0.6 on 2018-07-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_auto_20180727_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'text (multiple line)'), ('short-text', 'short text (one line)'), ('radio', 'radio')], default='text', max_length=200, verbose_name='Type'),
        ),
    ]
