# Generated by Django 5.1.2 on 2024-10-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(choices=[(True, 'SuperUser'), (False, 'Staff')], default=False),
        ),
    ]
