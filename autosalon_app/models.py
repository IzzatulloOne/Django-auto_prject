from django.db import models


class Brands(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=30, unique=True, verbose_name="Название бренда") 
    country_of_origin = models.CharField(max_length=55, verbose_name="Страна происхождения") 
    year_founded = models.PositiveSmallIntegerField(verbose_name="Год основания") 
    founder = models.CharField(max_length=150, null=True, blank=True, verbose_name="Основатель") 
    logo = models.ImageField(upload_to='brand_logo/', verbose_name="Логотип") 

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        unique_together = ['name']
        ordering = ['-id']


class Cars(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    model_name = models.CharField(max_length=55, unique=True, verbose_name="Модель") 
    year_of_issue = models.PositiveSmallIntegerField(verbose_name="Год выпуска") 
    BODY_TYPE_CHOICES = [
        ('SD', 'Sedan'), ('HB', 'Hatchback'), ('SUV', 'SUV'), ('CP', 'Coupe'),
        ('CT', 'Convertible'), ('ET', 'Estate'), ('CR', 'Crossover'),
        ('MPV', 'Multi-Purpose Vehicle'), ('PT', 'Pickup Truck'), ('Van', 'Van'),
    ]
    ENGINE_CHOICES = [
        ('petrol', 'Petrol'), ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'), ('electric', 'Electric'),
    ]
    TRANSMISSIONS_CHOICES = [
        ('MT', 'Manual'), ('AT', 'Automatic'),
        ('CVT', 'Continuously Variable'), ('DCT', 'Dual Clutch'),
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
    staff = models.CharField(max_length=10, choices=STAFF, verbose_name="Дилер")
    drive = models.CharField(max_length=10, choices=DRIVE_CHOICES, verbose_name="Привод")
    transmissions = models.CharField(max_length=10, choices=TRANSMISSIONS_CHOICES, verbose_name="Коробка передач")
    engine = models.CharField(max_length=10, choices=ENGINE_CHOICES, verbose_name="Тип двигателя")
    body_type = models.CharField(max_length=10, choices=BODY_TYPE_CHOICES, verbose_name="Кузов")    
    engine_volume = models.FloatField(help_text="Объем двигателя в литрах", verbose_name="Объем двигателя")  
    engine_power = models.IntegerField(help_text="Мощность двигателя в л.с.", verbose_name="Мощность")  
    acceleration = models.FloatField(help_text="Разгон 0-100 км/ч (сек)", verbose_name="Разгон (0-100)")  
    maximum_speed = models.IntegerField(help_text="Максимальная скорость (км/ч)", verbose_name="Макс. скорость")  
    weight = models.IntegerField(help_text="Масса автомобиля (кг)", verbose_name="Вес")  
    price = models.FloatField(help_text="Цена автомобиля в $", verbose_name="Цена")  
    price_negotiable = models.BooleanField(verbose_name="Торг уместен") 
    photo = models.ImageField(upload_to='car_photos/', verbose_name="Фото")
    car_brand = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name="Бренд") 

    def __str__(self):
        return self.model_name
    
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-id']
        unique_together = ['model_name']


class Comment(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="comments", verbose_name="Автомобиль")
    name = models.CharField(max_length=50, verbose_name="Имя")
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.name} → {self.car.model_name}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]
