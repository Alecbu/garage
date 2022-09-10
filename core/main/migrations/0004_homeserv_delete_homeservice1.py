# Generated by Django 4.1.1 on 2022-09-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_homeservice1'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeServ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='HomeServ name')),
                ('name1', models.CharField(max_length=30, verbose_name='HomeServname1')),
                ('name2', models.CharField(max_length=30, verbose_name='HomeServ name2')),
                ('name3', models.CharField(max_length=30, verbose_name='HomeServ name3')),
                ('name4', models.CharField(max_length=30, verbose_name='HomeServ name4')),
                ('name5', models.CharField(max_length=30, verbose_name='HomeServ name5')),
                ('about', models.TextField(verbose_name='HomeServ about')),
            ],
            options={
                'verbose_name': 'HomeServ',
                'verbose_name_plural': 'HomeServs',
            },
        ),
        migrations.DeleteModel(
            name='HomeService1',
        ),
    ]
