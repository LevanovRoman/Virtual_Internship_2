from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100, verbose_name='Почта')
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    otc = models.CharField(max_length=50, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Контактный телефон')

    def __str__(self):
        return f'{self.fam} {self.name} {self.email}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Coordinates(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f"широта: {self.latitude}, долгота: {self.longitude}, высота: {self.height}"

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"


class Level(models.Model):
    winter = models.CharField(max_length=2, verbose_name='Зима', blank=True)
    summer = models.CharField(max_length=2, verbose_name='Лето', blank=True)
    autumn = models.CharField(max_length=2, verbose_name='Осень', blank=True)
    spring = models.CharField(max_length=2, verbose_name='Весна', blank=True)

    def __str__(self):
        return f"зима: {self.winter}, весна: {self.spring}, лето: {self.summer}, осень: {self.autumn}"

    class Meta:
        verbose_name = "Уровень сложности"
        verbose_name_plural = "Уровни сложности"


class Pereval(models.Model):
    NEW = "New"
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    STATUS_CHOICES = [
        ("New", "новый"),
        ("Pending", "в работе"),
        ("Accepted", "принят"),
        ("Rejected", "отклонен"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    coordinates = models.OneToOneField(Coordinates, on_delete=models.CASCADE, verbose_name='Координаты')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW, verbose_name='Статус')
    beauty_title = models.CharField(max_length=100, blank=True, verbose_name='Основное название вершины')
    title = models.CharField(max_length=100, verbose_name='Название вершины')
    other_titles = models.CharField(max_length=100, blank=True, verbose_name='Другое название')
    connect = models.CharField(max_length=100, blank=True, verbose_name='Связывает')
    add_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}: {self.beauty_title}"

    class Meta:
        verbose_name = "Перевал"
        verbose_name_plural = "Перевалы"


class Image(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    data = models.CharField(max_length=255, verbose_name='Изображение',
                            null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="Название")

    def __str__(self):
        return f"{self.pk}: {self.title}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
