from django.contrib import admin
from .models import Brands, Cars


admin.site.register(Brands)
admin.site.register(Cars)


class BrandsAdmin(admin.ModelAdmin):
    list_display = ("name", "country_of_origin", "year_founded", "founder")
    list_filter = ("country_of_origin", "year_founded")   # фильтры справа
    search_fields = ("name", "country_of_origin")        # поиск сверху


class CarsAdmin(admin.ModelAdmin):
    list_display = ("model_name", "car_brand", "year_of_issue", "engine", "body_type", "price")
    list_filter = ("car_brand", "engine", "body_type", "drive", "price_negotiable")
    search_fields = ("model_name", "car_brand__name")