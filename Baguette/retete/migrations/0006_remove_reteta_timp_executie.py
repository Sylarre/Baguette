# Generated by Django 3.0.2 on 2020-01-23 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retete', '0005_auto_20200123_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reteta',
            name='timp_executie',
        ),
    ]
