# Generated by Django 3.0.2 on 2020-01-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retete', '0004_auto_20200123_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reteta',
            name='timp_executie',
            field=models.TextField(),
        ),
    ]
