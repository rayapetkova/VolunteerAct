from django.contrib import admin

from VolunteerAct.categories.models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass