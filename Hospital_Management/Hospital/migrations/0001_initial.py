# Generated by Django 3.1.2 on 2020-10-30 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('Address', models.TextField()),
                ('Phonenumber', models.IntegerField()),
                ('Disease', models.TextField()),
                ('prescribtion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=25)),
                ('speciality', models.CharField(max_length=25)),
                ('img', models.ImageField(upload_to='pics')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
