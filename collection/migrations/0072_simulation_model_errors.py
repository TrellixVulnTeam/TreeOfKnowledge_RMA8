# Generated by Django 2.0.8 on 2019-07-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0071_simulation_model_just_learned_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation_model',
            name='errors',
            field=models.TextField(null=True),
        ),
    ]
