# Generated by Django 4.1.1 on 2022-09-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='HomeService name')),
                ('about', models.TextField(verbose_name='HomeService about')),
            ],
            options={
                'verbose_name': 'HomeService',
                'verbose_name_plural': 'HomeServices',
            },
        ),
    ]
