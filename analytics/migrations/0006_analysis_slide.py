# Generated by Django 3.2.7 on 2021-09-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_alter_symbol_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='slide',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Слайд'),
        ),
    ]
