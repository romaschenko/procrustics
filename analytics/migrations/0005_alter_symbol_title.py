# Generated by Django 3.2.7 on 2021-09-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_auto_20210920_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
