# Generated by Django 5.0.6 on 2024-06-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmgt_app', '0002_alter_expense_date_of_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='interest',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loan',
            name='no_installments',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loan',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
