from django.contrib import admin
from app.models import Food, FoodCategory, Notification


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('name',)
    ordering = ('sort',)


class FoodAdmin(admin.ModelAdmin):
    #inlines = (FoodReplacementInline,)
    list_display = ('name', 'category', 'calories', 'date_added')
    list_filter = ('category', 'date_added')
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('replacements',)


admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Notification)