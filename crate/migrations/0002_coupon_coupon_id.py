# Generated by Django 3.2.5 on 2021-08-06 13:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('crate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='coupon_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=254, unique=True),
        ),
    ]
