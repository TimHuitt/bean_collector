# Generated by Django 5.0.1 on 2024-01-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('origin', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=250)),
                ('cooking_time', models.CharField(max_length=50)),
                ('image', models.TextField(max_length=250)),
                ('common_uses', models.TextField(max_length=250)),
                ('nutritional_info', models.TextField(max_length=250)),
            ],
        ),
    ]
