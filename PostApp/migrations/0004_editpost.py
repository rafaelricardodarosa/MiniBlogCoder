# Generated by Django 4.0.5 on 2022-07-18 19:28

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0003_alter_comment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('subtitle', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PostApp.category')),
            ],
        ),
    ]
