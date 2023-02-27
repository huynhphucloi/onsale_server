from django.contrib import admin
from .models import Shop, ShopGroup

admin.site.site_header = "On Sale Locator"
admin.site.site_title = "On Sale Locator"
admin.site.index_title = "On Sale Locator"


class ShopAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'password', 'shop_group')
    search_fields = ['name', 'password']
    list_filter = ['shop_group']
    readonly_fields = ['password']
    fieldsets = (
        ("Shop Information", {
            'fields': ('name', 'password', 'open_hour', 'close_hour')
        }),
        ("Location", {
            'fields': ('google_maps', 'distance')
        }),
        ("Message", {
            'fields': ('url', 'message', 'message_two')
        }),
        ("Owner", {
            'fields': ('shop_group',)
        })
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['password']
        return []


class ShopGroupAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'password')
    search_fields = ['name', 'password']
    readonly_fields = ['password']


    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['password']
        return []


# Register your models here.
admin.site.register(Shop, ShopAdmin)
admin.site.register(ShopGroup, ShopGroupAdmin)
