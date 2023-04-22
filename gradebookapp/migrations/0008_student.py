# Generated by Django 4.1.7 on 2023-04-22 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebookapp', '0007_class_lecturer_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('DOB', models.DateField()),
            ],
        ),
    ]
