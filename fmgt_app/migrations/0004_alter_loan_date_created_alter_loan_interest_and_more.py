# Generated by Django 5.0.6 on 2024-06-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmgt_app', '0003_loan_interest_loan_no_installments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='interest',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='loan',
            name='no_installments',
            field=models.PositiveIntegerField(),
        ),
    ]
