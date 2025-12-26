from django.db import models


class Booking(models.Model):
    """Заявка на запись."""

    SERVICE_CHOICES = [
        ('therapy', 'Лечебный массаж'),
        ('relax', 'Расслабляющий массаж'),
        ('anticell', 'Антицеллюлитный массаж'),
        ('back', 'Массаж спины'),
    ]

    name = models.CharField('Имя', max_length=80)
    phone = models.CharField('Телефон', max_length=32)
    service = models.CharField('Услуга', max_length=32, choices=SERVICE_CHOICES)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self) -> str:
        return f"{self.name} ({self.get_service_display()})"


class Review(models.Model):
    """Отзыв клиента."""

    name = models.CharField('Имя', max_length=80)
    rating = models.PositiveSmallIntegerField('Оценка', default=5)
    text = models.TextField('Текст отзыва')
    created_at = models.DateTimeField('Дата', auto_now_add=True)
    is_published = models.BooleanField('Опубликован', default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self) -> str:
        return f"{self.name} — {self.rating}/5"

    @property
    def stars(self) -> str:
        r = max(0, min(int(self.rating), 5))
        return '★' * r + '☆' * (5 - r)
