# Generated by Django 5.0.2 on 2024-02-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0002_teacher_alter_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('experience', models.CharField(max_length=20)),
            ],
        ),
    ]
