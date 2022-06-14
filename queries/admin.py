from django.contrib import admin
from .models import Query


# Register your models here.
class QueryAdmin(admin.ModelAdmin):
    list_display = ['query_date', 'id', 'name']
    list_filter = ('name', 'query_date')


admin.site.register(Query, QueryAdmin)
