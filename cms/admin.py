from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider

class CMSAdmin(admin.ModelAdmin):
    list_display = ('c_title', 'c_text', 'c_css', 'get_img')
    list_editable = ('c_css',)
    list_display_links = ('c_title',)
    fields = ('c_title', 'c_text', 'c_css', 'c_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.c_img:
            return mark_safe(f'<img src="{obj.c_img.url}" width="80px"')
        else:
            return 'Нема світлини'

    get_img.short_description = 'Зображення'



admin.site.register(CmsSlider, CMSAdmin)
