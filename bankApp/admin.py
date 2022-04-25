from django.contrib import admin

# Register your models here.
from .models import cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'saldo')


admin.site.register(cliente, ClienteAdmin)
