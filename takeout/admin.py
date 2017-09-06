from django.contrib import admin
from takeout.models import topMenu, secondMenu, Food, Banner


class foodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'time', 'isright', 'menu']

admin.site.register(topMenu)
admin.site.register(secondMenu)
admin.site.register(Food, foodAdmin)
admin.site.register(Banner)