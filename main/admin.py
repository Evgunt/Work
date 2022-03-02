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


class keysModel(admin.ModelAdmin):
    fields = [('number', 'name'), ('tariff', 'date'),
              'owner', 'checkNum']


class requisitesModel(admin.ModelAdmin):
    fields = ['org', ('inn', 'kpp', 'company', 'address'), ('contacts', 'email', 'phone'),
              'docs', ('bank', 'checking', 'bic', 'checkingCo'), 'ogrn']


admin.site.unregister(Group)
admin.site.register(models.AdvUser, UserAdmin)
admin.site.register(models.keys, keysModel)
admin.site.register(models.tariffs, tarifModel)
admin.site.register(models.requisites, requisitesModel)
admin.site.register(models.checks)

