# Generated by Django 4.1.7 on 2023-04-22 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='classes',
            field=models.ManyToManyField(related_name='lecturers', to='gradebookapp.class'),
        ),
        migrations.AddField(
            model_name='semester',
            name='semester',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='semester',
            name='year',
            field=models.IntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='semester',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
