# Generated by Django 3.2.4 on 2021-07-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_invoice_bank_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='is_credited',
            field=models.BooleanField(default=False),
        ),
    ]
