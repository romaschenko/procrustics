# Generated by Django 3.2.7 on 2021-09-26 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0011_delete_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('price_when_issued', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('current_price', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('status_updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата обновления')),
                ('target_price_lt', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('status_changed_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='analytics.action')),
                ('status_lt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lt', to='analytics.status')),
                ('status_mt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mt', to='analytics.status')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='analytics.symbol', verbose_name='Тикер TV')),
            ],
        ),
    ]
