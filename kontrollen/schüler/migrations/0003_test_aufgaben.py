# Generated by Django 5.0 on 2024-01-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schüler', '0002_test_fach_alter_test_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='aufgaben',
            field=models.JSONField(default=list),
        ),
    ]
