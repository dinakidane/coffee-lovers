# Generated by Django 3.2.23 on 2024-02-08 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20240208_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='original_content',
        ),
    ]
