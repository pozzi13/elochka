from __future__ import annotations

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import BookingForm, ReviewForm
from .models import Review


def home(request: HttpRequest) -> HttpResponse:
    # последние 3 опубликованных отзыва
    reviews = Review.objects.filter(is_published=True)[:3]
    return render(
        request,
        'core/index.html',
        {
            'reviews': reviews,
        },
    )

def index(request):
    reviews = Review.objects.filter(is_published=True)[:3]  # последние 3 на главной
    return render(request, "index.html", {
        "reviews": reviews,
    })

def reviews(request):
    reviews = Review.objects.filter(is_published=True)
    return render(request, "reviews.html", {
        "reviews": reviews,
    })

def contacts(request):
    return render(request, "contacts.html")

def services_prices(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/uslugi_i_ceny.html')


def contacts_reviews(request: HttpRequest) -> HttpResponse:
    reviews = Review.objects.filter(is_published=True)
    form = ReviewForm()
    return render(
        request,
        'core/kontakty_i_otzyvy.html',
        {
            'reviews': reviews,
            'review_form': form,
        },
    )

def reviews_page(request):
    reviews = Review.objects.filter(is_published=True)
    form = ReviewForm()
    return render(request, "core/reviews.html", {"reviews": reviews, "review_form": form})

def contacts_page(request):
    return render(request, "core/contacts.html")

def booking_create(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return redirect('core:home')

    form = BookingForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Заявка отправлена! Мы свяжемся с вами в ближайшее время.')
    else:
        messages.error(request, 'Проверьте данные формы записи (есть ошибки).')

    return redirect(f"{reverse('core:home')}#booking")


def review_create(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return redirect('core:reviews')

    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.is_published = True
        review.save()
        messages.success(request, 'Спасибо! Отзыв отправлен и появится на сайте после модерации.')
    else:
        messages.error(request, 'Не получилось отправить отзыв. Проверьте поля формы.')

    return redirect(f"{reverse('core:reviews')}#reviews")


def sitemap_html(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/sitemap.html')


def robots_txt(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/robots.txt', content_type='text/plain; charset=utf-8')


def sitemap_xml(request: HttpRequest) -> HttpResponse:
    # Очень простой sitemap на 3 страницы
    base = request.build_absolute_uri('/')[:-1]
    urls = [
        base + reverse('core:home'),
        base + reverse('core:reviews'),
        base + reverse('core:contacts'),
    ]
    return render(
        request,
        'core/sitemap.xml',
        {
            'urls': urls,
        },
        content_type='application/xml; charset=utf-8',
    )
