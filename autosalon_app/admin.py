from django.contrib import admin
from django.utils.html import format_html
from .models import Brands, Cars, Comment


class CarsInline(admin.TabularInline):  # Inline для бренда
    model = Cars
    extra = 1


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country_of_origin", "year_founded", "founder", "logo_preview")  
    list_display_links = ("id", "name")  
    search_fields = ("name", "country_of_origin", "founder")  
    list_editable = ("country_of_origin", "year_founded")  
    list_filter = ("country_of_origin", "year_founded")  
    inlines = [CarsInline]  

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: contain;" />', obj.logo.url)
        return "No Logo"
    logo_preview.short_description = "Лого"


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = (
        "id", "model_name", "car_brand", "year_of_issue", 
        "body_type", "engine", "engine_volume", "engine_power",
        "maximum_speed", "price", "price_negotiable", "photo_preview"
    )
    list_display_links = ("id", "model_name")  
    search_fields = ("model_name", "car_brand__name")  
    list_editable = ("price", "price_negotiable")  
    list_filter = ("body_type", "engine", "drive", "transmissions", "car_brand")  

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="70" height="50" style="object-fit: cover;" />', obj.photo.url)
        return "No Photo"
    photo_preview.short_description = "Фото"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "car", "name", "text", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "text", "car__model_name")
    list_filter = ("created_at", "car")
