# Generated by Django 4.2.3 on 2023-07-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_schema',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
