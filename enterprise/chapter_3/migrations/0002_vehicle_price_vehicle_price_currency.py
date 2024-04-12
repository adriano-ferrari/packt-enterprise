# Generated by Django 4.0 on 2024-04-12 21:32

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('USD', 'USD $')], default='USD', editable=False, max_length=3, null=True),
        ),
    ]
