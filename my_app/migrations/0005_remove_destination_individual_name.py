# Generated by Django 2.2.2 on 2019-08-08 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_destination_individual_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination_individual',
            name='name',
        ),
    ]
