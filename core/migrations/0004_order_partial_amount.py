# Generated by Django 4.2.11 on 2025-06-15 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_order_payment_method_order_payment_proof_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='partial_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
