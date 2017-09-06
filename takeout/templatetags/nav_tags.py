from django import template
from takeout.models import topMenu, secondMenu, Banner, Food

register = template.Library()

@register.simple_tag
def get_top_menu():
	return topMenu.objects.all()

@register.simple_tag
def get_second_menu(top):
	# if top: return secondMenu.objects.filter(top__name=top)
	# else: return secondMenu.objects.all()
	return secondMenu.objects.filter(top__name=top) if top else secondMenu.objects.all()

@register.simple_tag
def get_banner():
	return Banner.objects.all().order_by('position')

@register.simple_tag
def get_hot_food():
	return Food.objects.filter(isright=True).order_by('-time')[:3]
	 