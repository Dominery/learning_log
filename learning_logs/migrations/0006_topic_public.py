# Generated by Django 2.2.2 on 2020-12-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_entry_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='public',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
