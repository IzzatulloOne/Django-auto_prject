from django.db import models


class Brands(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30 , unique=True) # например Nissan, Toyota, BMW
    country_of_origin = models.CharField(max_length=55)# например Япония, Германия, США
    year_founded = models.PositiveSmallIntegerField()# например чтобы знать историю бренда
    founder = models.CharField(max_length=150,null=True, blank=True)# например необязательно, но красиво
    logo = models.ImageField(upload_to='brand_logo/')# например ссылка или файл

    def __str__(self):
        return self.name


class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=55, unique=True) # например GTR R35
    year_of_issue = models.PositiveSmallIntegerField() #например 2009 
    BODY_TYPE_CHOICES = [
        ('SD', 'Sedan'),
        ('HB', 'Hatchback'),
        ('SUV', 'SUV'),
        ('CP', 'Coupe'),
        ('CT', 'Convertible'),
        ('ET', 'Estate'),
        ('CR', 'Crossover'),
        ('MPV', 'Multi-Purpose Vehicle'),
        ('PT', 'Pickup Truck'),
        ('Van', 'Van'),
    ]
    ENGINE_CHOICES = [
    ('petrol', 'Petrol'),
    ('diesel', 'Diesel'),
    ('hybrid', 'Hybrid'),
    ('electric', 'Electric'),
    ]

    TRANSMISSIONS_CHOICES = [
        ('MT', 'Manual Transmission'),
        ('AT', 'Automatic Transmission'),
        ('CVT', 'Continuously Variable Transmission'),
        ('DCT', 'Dual Clutch Transmission'),
    ]

    DRIVE_CHOICES = [
        ('RWD', 'Rear wheel drive'),
        ('FWD', 'Front wheel drive'),
        ('AWD', 'All wheel drive'),
    ]
    STAFF = [
        ('OD', 'Official dealer'),
        ('NOD', 'Not official dealer'),
    ]
    staff = models.CharField(max_length=10, choices=STAFF)
    drive = models.CharField(max_length=10, choices=DRIVE_CHOICES)
    transmissions = models.CharField(max_length=10, choices=TRANSMISSIONS_CHOICES)
    engine = models.CharField(max_length=10, choices=ENGINE_CHOICES)
    body_type = models.CharField(max_length=10, choices=BODY_TYPE_CHOICES)    
    engine_volume = models.FloatField(help_text="Объем двигателя в литрах")  
    engine_power = models.IntegerField(help_text="Мощность двигателя в лошадиных силах (HP)")  
    acceleration = models.FloatField(help_text="Разгон 0-100 км/ч (сек)")  
    maximum_speed = models.IntegerField(help_text="Максимальная скорость (км/ч)")  
    weight = models.IntegerField(help_text="Масса автомобиля (кг)")  
    price = models.FloatField(help_text="Цена автомобиля в долларах США")  
    price_negotiable = models.BooleanField() 
    photo = models.ImageField(upload_to='car_photos/')
    car_brand = models.ForeignKey(Brands, on_delete=models.CASCADE) 

    def __str__(self):
        return self.model_name