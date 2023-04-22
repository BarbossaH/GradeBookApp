# Generated by Django 4.1.7 on 2023-04-22 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gradebookapp', '0009_enrollment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollTime', models.DateField(auto_created=True)),
                ('studentId', models.IntegerField(max_length=100)),
                ('classId', models.IntegerField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('gradeTime', models.DateField()),
                ('enrolled_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebookapp.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradebookapp.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
    ]
