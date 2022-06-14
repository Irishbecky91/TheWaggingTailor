from django.contrib import admin
from .models import UsersProfile, PetProfile


class PetProfileInline(admin.TabularInline):
    """
    Pet Profile Admin
    """
    model = PetProfile


# Register your models here.
class UsersProfileAdmin(admin.ModelAdmin):
    """
    User Profile Admin
    """
    inlines = [PetProfileInline]
    list_display = (
        'user',
    )


admin.site.register(UsersProfile, UsersProfileAdmin)
