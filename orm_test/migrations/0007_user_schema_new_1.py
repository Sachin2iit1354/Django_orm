# Generated by Django 4.2.3 on 2023-09-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_test', '0006_user_schema_log_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_schema',
            name='new_1',
            field=models.TimeField(null=True),
        ),
    ]
