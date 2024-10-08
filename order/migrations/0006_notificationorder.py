# Generated by Django 5.1 on 2024-09-14 15:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_count', models.PositiveIntegerField(default=0, verbose_name='employee count')),
                ('durations_days', models.PositiveIntegerField(default=0, verbose_name='durations days')),
                ('box_count', models.PositiveIntegerField(default=0, verbose_name='box count')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_orders', to='order.order', verbose_name='order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_orders', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
