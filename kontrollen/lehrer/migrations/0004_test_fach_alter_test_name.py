# Generated by Django 5.0 on 2023-12-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lehrer', '0003_alter_test_jahrgang'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='fach',
            field=models.CharField(default='Mathematik', max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(default='', max_length=300),
        ),
    ]