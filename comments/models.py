# -*- coding: utf8 -*-
from django.db import models
from django.urls import reverse
from takeout.models import Food

class Comment(models.Model):
	text = models.TextField('内容', max_length=30)
	created_time = models.DateTimeField('发表时间', auto_now_add=True)
	food = models.ForeignKey('takeout.Food')
	user = models.ForeignKey('user.User')

	def __str__(self):
		return self.text[:10]

	def get_absolute_url(self):
		food = Food.objects.get(comment__created_time=self.created_time)
		return reverse('takeout:food', kwargs={'food_name': food.name})

	class Meta:
		ordering = ['-created_time']
		verbose_name = '评论'
		verbose_name_plural = '全部评论'