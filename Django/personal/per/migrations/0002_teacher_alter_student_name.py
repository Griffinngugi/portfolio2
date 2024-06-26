# Generated by Django 5.0.2 on 2024-02-26 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
