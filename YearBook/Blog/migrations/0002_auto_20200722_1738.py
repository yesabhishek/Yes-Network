# Generated by Django 3.0.8 on 2020-07-22 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]