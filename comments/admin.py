from django.contrib import admin
from comments.models import Comment

class commentAdmin(admin.ModelAdmin):
	list_display = ['user', 'text', 'created_time', 'food']

admin.site.register(Comment, commentAdmin)
