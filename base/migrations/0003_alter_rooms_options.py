# Generated by Django 4.2.4 on 2023-09-22 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_rooms_host_messeag_rooms_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rooms',
            options={'ordering': ['-updated', 'created']},
        ),
    ]