# Generated by Django 3.2.23 on 2024-02-08 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_comment_parent_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment',
        ),
    ]