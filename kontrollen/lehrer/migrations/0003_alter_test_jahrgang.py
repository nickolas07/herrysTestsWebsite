# Generated by Django 4.2.4 on 2023-09-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lehrer', '0002_test_jahrgang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='jahrgang',
            field=models.IntegerField(),
        ),
    ]