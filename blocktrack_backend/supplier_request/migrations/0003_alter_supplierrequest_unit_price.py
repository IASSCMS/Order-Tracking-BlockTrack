# Generated by Django 5.2 on 2025-05-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier_request', '0002_supplierrequest_is_defective_supplierrequest_quality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierrequest',
            name='unit_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
