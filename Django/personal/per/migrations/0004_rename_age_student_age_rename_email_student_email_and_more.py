# Generated by Django 5.0.2 on 2024-02-27 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0003_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='phone',
            new_name='Phone',
        ),
    ]
