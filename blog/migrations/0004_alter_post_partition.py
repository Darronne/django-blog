# Generated by Django 4.0.1 on 2022-01-27 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_partition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='partition',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.partition'),
        ),
    ]
