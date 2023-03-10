# Generated by Django 4.1.5 on 2023-01-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('rate', models.FloatField(default=0.0)),
            ],
        ),
    ]
