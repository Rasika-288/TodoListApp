# Generated by Django 3.2.4 on 2021-06-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0004_alter_note_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
