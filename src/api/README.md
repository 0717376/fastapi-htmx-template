# API Endpoints

HTTP endpoints (роуты) приложения.

## Что здесь:
- REST API endpoints
- HTMX endpoints для динамических страниц
- WebSocket handlers (если нужны)

## Структура:
```python
# users.py
@router.get("/users")
async def get_users():
    return await user_service.get_all()
```

## Правила:
- Один файл = один ресурс (users.py, posts.py)
- Минимум логики (вся в services)
- Только валидация и вызов сервисов