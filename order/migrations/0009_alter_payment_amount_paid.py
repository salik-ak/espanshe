# Generated by Django 3.2.16 on 2023-03-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_payment_amount_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount_paid',
            field=models.FloatField(default=0),
        ),
    ]
