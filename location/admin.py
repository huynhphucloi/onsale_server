from django.contrib import admin
from .models import Shop

admin.site.site_header = "On Sale Locator"
admin.site.site_title = "On Sale Locator"
admin.site.index_title = "On Sale Locator"


class ShopAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'password', 'user')
    search_fields = ['name', 'password']
    list_filter = ['user']
    readonly_fields = ['password']
    fieldsets = (
        ("Shop Information", {
            'fields': ('name', 'password', 'open_hour', 'close_hour')
        }),
        ("Location", {
            'fields': ('google_maps', 'distance')
        }),
        ("Message", {
            'fields': ('url', 'message')
        }),
        ("Owner", {
            'fields': ('user',)
        })
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['password']
        return []


# Register your models here.
admin.site.register(Shop, ShopAdmin)
