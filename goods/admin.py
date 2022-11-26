from django.contrib import admin
from .models import Media, Genre, Status, Product

# from .models import Product
# admin.site.register(Product)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'height', 'weight', 'photo', 'buy_url', 'description', 'genre', 'status', 'media')

