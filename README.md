# Сайт «Ёлочка» — Django + ваш HTML/CSS

Этот проект **берёт ваш готовый фронтенд** (index.html + style.css + script.js) и добавляет **бекенд на Django**:

- 3 страницы (как просили: не раздуваем):
  - `/` — главная (ваш лендинг)
  - `/uslugi-i-ceny/` — услуги и цены
  - `/kontakty-i-otzyvy/` — контакты + реальные отзывы + форма добавления
- Админка `/admin/`:
  - заявки на запись
  - отзывы (с модерацией: галочка "Опубликован")
- `robots.txt`, `sitemap.xml`, `sitemap.html`.

## Запуск локально

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

## Как устроены отзывы

- Отзыв добавляется через форму на странице `/kontakty-i-otzyvy/`.
- По умолчанию он попадает на модерацию (`Опубликован = False`).
- Чтобы отзыв появился на сайте — зайди в админку и поставь галочку **Опубликован**.

## Где лежит ваш фронтенд

- CSS/JS взяты **без правок** и лежат в папке `static/`:
  - `static/style.css`
  - `static/script.js`

Шаблоны страниц в `core/templates/core/`.
