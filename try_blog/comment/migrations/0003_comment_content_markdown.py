# Generated by Django 2.2 on 2019-10-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20191005_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content_markdown',
            field=models.CharField(default='这是一次性默认值，该字段要非空', max_length=2000, verbose_name='md内容'),
            preserve_default=False,
        ),
    ]
