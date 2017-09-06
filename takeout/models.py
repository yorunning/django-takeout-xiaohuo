# -*- coding: utf8 -*-
from django.db import models
from django.urls import reverse

# Create your models here.

class topMenu(models.Model):
	name = models.CharField('菜系名', max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '顶级菜系(仅修改)'
		verbose_name_plural = '顶级菜系'

class secondMenu(models.Model):
	name = models.CharField('菜系名', max_length=50)
	image = models.CharField('dock图', max_length=100)
	top = models.ForeignKey(topMenu)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '二级菜系'
		verbose_name_plural = '二级菜系'

class Food(models.Model):
	name = models.CharField('菜名', max_length=100)
	price = models.IntegerField('单价')
	time = models.DateTimeField('创建时间')
	image = models.CharField('图片地址', max_length=500)
	introduce = models.TextField('介绍', max_length=100, blank=True)
	isright = models.BooleanField('是否推到首页', default=False)
	menu = models.ForeignKey(secondMenu)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('takeout:food', kwargs={'food_name': self.name})

	class Meta:
		ordering = ['-time']
		verbose_name = '菜单'
		verbose_name_plural = '菜单'

class Banner(models.Model):
	position = models.CharField('位置', max_length=10)
	image = models.CharField('图片地址', max_length=500)

	def __str__(self):
		return self.position

	class Meta:
		verbose_name = '轮播图(五张)'
		verbose_name_plural = '轮播图'