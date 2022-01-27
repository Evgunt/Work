from django.contrib import admin
from django.contrib.auth.models import Group, User

from . import models

admin.site.site_header = 'Панель администрирования Велокрюк'

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(models.pages)
admin.site.register(models.slider)
admin.site.register(models.gallery)


class photos(admin.TabularInline):
    model = models.photos


class servicesAdm(admin.ModelAdmin):
    inlines = [photos]


class UserAdmin(admin.ModelAdmin):
    fields = ['email', ('first_name', 'last_name'), ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


class firstBlock(admin.ModelAdmin):
    model = models.firstBlock

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(models.firstBlock, firstBlock)
admin.site.register(models.services, servicesAdm)
admin.site.register(User, UserAdmin)
