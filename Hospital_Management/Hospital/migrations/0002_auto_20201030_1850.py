# Generated by Django 3.1.2 on 2020-10-30 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='speciality',
            new_name='speciality_job',
        ),
    ]