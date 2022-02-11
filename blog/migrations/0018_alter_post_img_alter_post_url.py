# Generated by Django 4.0.1 on 2022-02-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]