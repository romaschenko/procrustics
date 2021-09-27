# Generated by Django 3.2.7 on 2021-09-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0009_action_rating_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='current_price',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='price_when_issued',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='target_price_lt',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]
