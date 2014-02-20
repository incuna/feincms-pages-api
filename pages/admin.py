from django.contrib import admin
from feincms.admin.item_editor import ItemEditor
from feincms.extensions import ExtensionModelAdmin
from orderable.admin import OrderableTabularInline

from . import models


class PageAdmin(ItemEditor, ExtensionModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'slug'],
        }),
        # <-- extensions appear here, see fieldset_insertion_index.
    ]
    fieldset_insertion_index = 1
    filter_horizontal = []
    list_display = ['name', 'slug']
    list_filter = []
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name', 'slug']


class GroupItemInline(OrderableTabularInline):
    model = models.GroupItem


class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupItemInline]


admin.site.register(models.Page, PageAdmin)
admin.site.register(models.Group, GroupAdmin)
