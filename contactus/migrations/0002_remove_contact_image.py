# Generated by Django 4.2.1 on 2023-05-05 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
    ]
