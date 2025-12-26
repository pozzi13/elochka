# Generated manually for учебный проект

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Имя')),
                ('phone', models.CharField(max_length=32, verbose_name='Телефон')),
                ('service', models.CharField(choices=[('therapy', 'Лечебный массаж'), ('relax', 'Расслабляющий массаж'), ('anticell', 'Антицеллюлитный массаж'), ('back', 'Массаж спины')], max_length=32, verbose_name='Услуга')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Имя')),
                ('rating', models.PositiveSmallIntegerField(default=5, verbose_name='Оценка')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-created_at'],
            },
        ),
    ]
