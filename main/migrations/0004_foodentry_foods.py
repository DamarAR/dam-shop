# Generated by Django 5.1.1 on 2024-09-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_foodentry_foods'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodentry',
            name='foods',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
