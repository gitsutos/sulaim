# Generated by Django 3.2.7 on 2021-11-24 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0011_auto_20211124_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costlist',
            name='added_date',
        ),
    ]
