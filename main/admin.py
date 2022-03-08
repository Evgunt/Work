from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import Q

from . import models

admin.site.site_header = 'Панель администрирования Ceramic 3D'


class UserAdmin(admin.ModelAdmin):
    fields = [('email', 'phone'), 'first_name',  'send_messages',
              ('region', 'time', 'language')]

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.username != 'root':
            return qs.filter(~Q(username='root') & ~Q(username='Отсутствует'))
        else:
            return qs


class tarifModel(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.username != 'root':
            return qs.filter(~Q(name='Отсутствует'))
        else:
            return qs


class help_files(admin.TabularInline):
   model = models.Files_helps


class keysModel(admin.ModelAdmin):
    fields = [('number', 'name'), ('tariff', 'date'),
              'owner', 'checkNum']


class requisitesModel(admin.ModelAdmin):
    fields = ['org', ('inn', 'kpp', 'company', 'address'), ('contacts', 'email', 'phone'),
              'docs', ('bank', 'checking', 'bic', 'checkingCo'), 'ogrn', 'owner']
    
    def has_change_permission(self, request, obj=None):
        return False    

    def has_dellete_permission(self, request, obj=None):
        return False


class helpMessageModel(admin.ModelAdmin):
    inlines = (help_files,)

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.unregister(Group)
admin.site.register(models.AdvUser, UserAdmin)
admin.site.register(models.keys, keysModel)
admin.site.register(models.tariffs, tarifModel)
admin.site.register(models.requisites, requisitesModel)
admin.site.register(models.checks)
admin.site.register(models.helpMessage, helpMessageModel)

