# Generated by Django 5.1.4 on 2025-01-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_doctor_doc_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
