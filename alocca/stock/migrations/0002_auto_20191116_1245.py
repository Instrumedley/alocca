# Generated by Django 2.2.7 on 2019-11-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='holding_value',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='total_profit_loss',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='profit_loss',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
