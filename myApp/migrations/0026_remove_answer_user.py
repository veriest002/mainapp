# Generated by Django 2.0.6 on 2018-08-12 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0025_answer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
    ]
