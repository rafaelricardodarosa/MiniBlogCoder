# Generated by Django 4.0.5 on 2022-07-19 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0004_editpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='editpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]