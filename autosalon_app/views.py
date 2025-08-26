from django.shortcuts import render, get_object_or_404
from .models import Brands, Cars


from django.shortcuts import render
from .models import Brands, Cars

from django.shortcuts import render
from .models import Brands, Cars

from django.shortcuts import render
from .models import Brands, Cars

from django.shortcuts import render
from .models import Brands, Cars

def all(request):
    brands = Brands.objects.all()
    cars = Cars.objects.all()

    # Фильтры
    brand_id = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    body_type = request.GET.get('body_type')
    drive = request.GET.get('drive')
    year_from = request.GET.get('year_from')
    year_to = request.GET.get('year_to')
    sort = request.GET.get('sort')

    if brand_id and brand_id.isdigit():
        cars = cars.filter(car_brand_id=brand_id)
    if min_price:
        cars = cars.filter(price_dollars__gte=min_price)
    if max_price:
        cars = cars.filter(price_dollars__lte=max_price)
    if body_type:
        cars = cars.filter(body_type=body_type)
    if drive:
        cars = cars.filter(drive=drive)
    if year_from:
        cars = cars.filter(year_of_issue__gte=year_from)
    if year_to:
        cars = cars.filter(year_of_issue__lte=year_to)

    # Сортировка
    if sort == "price_asc":
        cars = cars.order_by("price_dollars")
    elif sort == "price_desc":
        cars = cars.order_by("-price_dollars")
    elif sort == "year_asc":
        cars = cars.order_by("year_of_issue")
    elif sort == "year_desc":
        cars = cars.order_by("-year_of_issue")
    elif sort == "power_desc":
        cars = cars.order_by("-engine_power")
    elif sort == "power_asc":
        cars = cars.order_by("engine_power")

    context = {
        'brand': brands,
        'car': cars
    }
    return render(request, 'auto_web/index.html', context)





def car_detail(request, car_id):
    brands = Brands.objects.all()
    car = get_object_or_404(Cars, id=car_id)

    context = {
        'brands': brands,
        'car': car,
    }
    return render(request, 'auto_web/detail.html', context)


def brand_category(request, brand_id):
    brands = Brands.objects.all()
    brand = get_object_or_404(Brands, id=brand_id)
    cars = Cars.objects.filter(car_brand_id=brand_id)

    context = {
        'brands': brands,
        'brand': brand,
        'cars': cars,
    }
    return render(request, 'auto_web/brand_category.html', context)
