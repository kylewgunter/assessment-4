# Generated by Django 3.2.5 on 2021-07-28 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='decription',
            new_name='description',
        ),
    ]
