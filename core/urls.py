from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("uslugi-i-ceny/", views.services_prices, name="services_prices"),
    path("kontakty-i-otzyvy/", views.contacts_reviews, name="contacts_reviews"),

    path("reviews/", views.reviews_page, name="reviews"),
    path("contacts/", views.contacts_page, name="contacts"),

    path("booking/", views.booking_create, name="booking_create"),
    path("review/", views.review_create, name="review_create"),

    path("sitemap.xml", views.sitemap_xml, name="sitemap_xml"),
    path("sitemap.html", views.sitemap_html, name="sitemap_html"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
