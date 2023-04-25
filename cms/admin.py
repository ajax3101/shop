from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CMSSlider


class CMSAdmin(admin.ModelAdmin):
    list_display = ('get_img', 'cms_title', 'cms_text', 'cms_css')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_img', 'get_img', 'cms_title', 'cms_text', 'cms_css')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px">')
        else:
            return f'No image!'

    get_img.short_description = 'Ì³í³àòþðà'


admin.site.register(CMSSlider, CMSAdmin)
