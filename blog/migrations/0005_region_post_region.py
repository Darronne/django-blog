# Generated by Django 4.0.1 on 2022-01-27 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_partition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='region',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.region'),
        ),
    ]
