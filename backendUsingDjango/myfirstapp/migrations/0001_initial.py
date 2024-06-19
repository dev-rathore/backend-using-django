# Generated by Django 5.0.6 on 2024-06-19 20:08

import django.utils.timezone
from django.db import migrations, models

class Migration(migrations.Migration):
  initial = True

  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='MyFirstModel',
      fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=100)),
        ('image', models.ImageField(upload_to='images/')),
        ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
        ('occupation', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('D', 'Developer'), ('O', 'Other')], max_length=1)),
      ],
    ),
  ]
