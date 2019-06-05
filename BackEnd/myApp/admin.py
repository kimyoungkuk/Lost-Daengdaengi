from django.contrib import admin
from .models import *
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Customizing
class Dog_shelterAdmin(admin.ModelAdmin):
    list_display = ['shelter_name', 'phone_num', 'description']
    list_display_links = ['shelter_name', 'phone_num', 'description']
    search_fields = ['shelter_name']

class Owner_postAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone_num', 'dog_name',
            'dog_sex', 'dog_type', 'dog_age', 'lost_time',
            'dog_feature', 'remark', 'image']
    list_filter = ('dog_sex', 'dog_type', 'dog_age',
            ('lost_time', DateRangeFilter),)
    search_fields = ['dog_name']

class Finder_postAdmin(admin.ModelAdmin):
    list_display = ['title','phone_num','posted_time','posted_due','find_time',
            'dog_feature','dog_type','shelter']
    list_filter = ('dog_type','shelter',('find_time', DateRangeFilter),)
    search_fields = ['dog_feature']

class UserAdmin(admin.ModelAdmin):
    list_display = ['nickname','key','is_admin']
    list_filter = ('is_admin',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Owner_post, Owner_postAdmin)
admin.site.register(Finder_post, Finder_postAdmin)
admin.site.register(Dog_shelter, Dog_shelterAdmin)

admin.site.register(Comment)
admin.site.register(Report)
admin.site.register(Adopt_post)
