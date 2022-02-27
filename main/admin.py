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
        return qs.filter(~Q(username='root') & ~Q(username='Отсутствует'))


admin.site.unregister(Group)
admin.site.register(models.AdvUser, UserAdmin)
admin.site.register(models.keys)
admin.site.register(models.tariffs)

