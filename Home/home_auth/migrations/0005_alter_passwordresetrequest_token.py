# Generated by Django 5.1.7 on 2025-07-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home_auth", "0004_alter_passwordresetrequest_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passwordresetrequest",
            name="token",
            field=models.CharField(
                default="VWE3SO9NvRC1ffdUFluUcweYIbWy8fGj",
                editable=False,
                max_length=32,
                unique=True,
            ),
        ),
    ]
