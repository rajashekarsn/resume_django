from django.contrib import admin
from .models import NavMenuItems, AboutInfo, Experience, Education, LanguagesTools, Interests, Awards, RoleBullets
from tinymce.widgets import TinyMCE
from django.db import models

class NavMenuItemsAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_link_href')


class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('about_first_name', 'about_second_name', 'about_address', 'about_mobile_number', 'about_email',
                    'about_description')


class RoleBulletsInline(admin.TabularInline):
     model = RoleBullets
     extra = 1
#
#
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'location', 'role_description', 'from_date', 'to_date')
    inlines = [
        RoleBulletsInline
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'university', 'specialization', 'percentage', 'from_date', 'to_date')


class LanguagesToolsAdmin(admin.ModelAdmin):
    list_display = ('description',)


class InterestsAdmin(admin.ModelAdmin):
    list_display = ('description',)


class AwardsAdmin(admin.ModelAdmin):
    list_display = ('award',)





admin.site.register(NavMenuItems, NavMenuItemsAdmin)
admin.site.register(AboutInfo, AboutInfoAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(LanguagesTools, LanguagesToolsAdmin)
admin.site.register(Interests, InterestsAdmin)
admin.site.register(Awards, AwardsAdmin)
