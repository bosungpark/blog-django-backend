# Generated by Django 3.2.5 on 2021-07-23 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='modify_date',
        ),
    ]
