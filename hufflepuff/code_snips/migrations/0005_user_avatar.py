# Generated by Django 3.2.9 on 2021-11-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_snips', '0004_auto_20211116_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.URLField(blank=True, null=True),
        ),
    ]
