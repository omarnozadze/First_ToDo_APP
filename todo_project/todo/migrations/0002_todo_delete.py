# Generated by Django 4.2.1 on 2023-06-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='delete',
            field=models.BooleanField(default=True),
        ),
    ]
