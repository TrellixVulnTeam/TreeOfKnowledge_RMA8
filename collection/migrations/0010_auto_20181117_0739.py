# Generated by Django 2.0.8 on 2018-11-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_auto_20181115_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation_model',
            name='specification',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='uploaded_dataset',
            name='specification',
            field=models.TextField(),
        ),
    ]