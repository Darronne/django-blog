# Generated by Django 4.0.1 on 2022-02-02 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(default=''),
        ),
    ]