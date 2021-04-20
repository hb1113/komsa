# Generated by Django 3.1.7 on 2021-04-20 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QuoteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotepost',
            name='comments',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quotepost',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quotepost',
            name='shares',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quotepost',
            name='text',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='QuoteComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('comments', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='QuoteApp.quotecomment')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotecomments', to='QuoteApp.quotepost')),
            ],
        ),
    ]
