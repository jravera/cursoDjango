# Generated by Django 3.2.25 on 2024-09-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='signature',
            field=models.TextField(default='Firma', max_length=100),
        ),
    ]
