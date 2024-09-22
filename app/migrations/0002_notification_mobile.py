# Generated by Django 5.0 on 2024-09-22 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="mobile",
            field=models.CharField(
                default="+6512345678",
                max_length=17,
                validators=[
                    django.core.validators.RegexValidator(
                        "^\\+?1?\\d{9,15}$",
                        "Mobile number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                    )
                ],
            ),
            preserve_default=False,
        ),
    ]
