# Generated by Django 3.1.4 on 2021-04-26 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteApp', '0005_auto_20210426_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotepost',
            name='comments',
        ),
    ]
