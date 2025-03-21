from django.contrib import admin

from VolunteerAct.categories.models import Category, Event


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('image', 'poster_img', 'name', 'short_description', 'long_description')

    search_fields = ('name', 'short_description')

    ordering = ('id', )

    list_filter = ('name', )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')

    list_filter = ('title', 'is_emergency')

    filter_horizontal = ('attendees', )
