# Services

Бизнес-логика приложения.

## Что здесь:
- CRUD операции с БД
- Сложная бизнес-логика
- Интеграции с внешними API
- Email отправка, работа с файлами

## Пример:
```python
# user_service.py
from models.user import User
from schemas.user import UserCreate

async def create_user(data: UserCreate) -> User:
    # Хешируем пароль
    hashed = hash_password(data.password)
    
    # Создаем пользователя
    user = User(
        email=data.email,
        username=data.username,
        password=hashed
    )
    
    # Сохраняем в БД
    db.add(user)
    await db.commit()
    
    return user
```

## Правила:
- Вся логика здесь, не в роутах
- Один сервис = один домен (users, posts, payments)
- Сервисы могут вызывать друг друга