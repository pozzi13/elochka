# Elochka Massage Salon Website

Django web application for a massage salon website.

## Features

- landing page with salon information
- services and pricing page
- contacts and reviews page
- booking form
- review submission form with moderation
- Django admin panel
- sitemap.xml, sitemap.html and robots.txt
- static files support with WhiteNoise

## Pages

- `/` — home page
- `/uslugi-i-ceny/` — services and pricing
- `/kontakty-i-otzyvy/` — contacts and reviews
- `/reviews/` — reviews page
- `/contacts/` — contacts page
- `/admin/` — admin panel

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- WhiteNoise

## Local setup

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Открыть:
- Главная: `http://127.0.0.1:8000/`
- Админка: `http://127.0.0.1:8000/admin/`

## Reviews moderation

- Users can submit reviews through the website form.
- New reviews are saved with is_published = False by default.

##To publish a review:
- open Django admin panel
- go to Reviews
- enable the Published checkbox
- save changes
Only published reviews are displayed on the website.

html from `core/templates/core/`.
