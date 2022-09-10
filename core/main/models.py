from ast import Delete
from enum import unique
from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField('Menu name', max_length=15)
    slug = models.SlugField('Home slug', unique=True ,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus' 
        

class Home(models.Model):
    img = models.ImageField('Home img', upload_to='media')
    slug = models.SlugField('Home slug', unique=True ,null=True)

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'  

class HomeIntro(models.Model):
    title = models.CharField('HomeIntro title', max_length=30)
    name = models.CharField('HomeIntro name', max_length=30)
    about = models.TextField('HomeIntro about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeIntro'
        verbose_name_plural = 'HomeIntros'

class HomeServ1(models.Model):
    name = models.CharField('HomeServ1 name', max_length=30)
    name1 = models.CharField('HomeServ1 name1', max_length=30)
    name2 = models.CharField('HomeServ1 name2', max_length=30)
    name3 = models.CharField('HomeServ1 name3', max_length=30)
    name4 = models.CharField('HomeServ1 name4', max_length=30)
    name5 = models.CharField('HomeServ1 name5', max_length=30)
    about = models.TextField('HomeServ1 about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeServ1'
        verbose_name_plural = 'HomeServ1s'

class HomeServ2(models.Model):
    name = models.CharField('HomeServ2 name', max_length=30)
    about = models.TextField('HomeServ2 about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeServ2'
        verbose_name_plural = 'HomeServ2s'

class HomeServ3(models.Model):
    name = models.CharField('HomeServ3 name', max_length=30)
    about = models.TextField('HomeServ3 about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeServ3'
        verbose_name_plural = 'HomeServ3s'

