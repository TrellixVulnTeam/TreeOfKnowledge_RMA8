# Generated by Django 2.0.8 on 2019-05-23 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0059_attribute_all_applicable_object_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='all_applicable_object_types',
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='all_relation_object_types',
        ),
    ]