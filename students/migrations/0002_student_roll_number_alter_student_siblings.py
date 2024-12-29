# Generated by Django 5.1.2 on 2024-12-29 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_number',
            field=models.CharField(blank=True, max_length=7, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='siblings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
    ]
