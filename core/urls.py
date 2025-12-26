from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),

    # 3 пользовательские страницы:
    path("reviews/", views.reviews_page, name="reviews"),
    path("review/", views.review_create, name="review_create"),
    path("contacts/", views.contacts_page, name="contacts"),

    # формы
    path("booking/", views.booking_create, name="booking_create"),
    path("review/", views.review_create, name="review_create"),

    # техничка
    path("sitemap.xml", views.sitemap_xml, name="sitemap_xml"),
    path("sitemap.html", views.sitemap_html, name="sitemap_html"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
