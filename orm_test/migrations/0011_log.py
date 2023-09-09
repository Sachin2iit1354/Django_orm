# Generated by Django 4.2.3 on 2023-09-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_test', '0010_alter_user_schema_new_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tendancy', models.CharField(max_length=200)),
                ('heading', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('log_time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]