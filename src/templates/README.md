# Templates

HTML шаблоны (Jinja2) для рендеринга страниц.

## Структура:
```
templates/
├── base/
│   └── layout.html      # Базовый шаблон
├── components/
│   ├── navbar.html      # Навигация
│   ├── card.html        # Карточка
│   └── modal.html       # Модальное окно
└── pages/
    ├── index.html       # Главная
    ├── login.html       # Вход
    └── dashboard.html   # Дашборд
```

## HTMX паттерны:
```html
<!-- Загрузка контента -->
<div hx-get="/api/users" hx-trigger="load">
    Загрузка...
</div>

<!-- Форма -->
<form hx-post="/api/users" hx-target="#result">
    <input name="email" type="email">
    <button>Отправить</button>
</form>
```

## Правила:
- Переиспользуемые компоненты в components/
- Страницы наследуют base/layout.html
- HTMX атрибуты для динамики