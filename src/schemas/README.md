# Schemas

Pydantic схемы для валидации входящих/исходящих данных.

## Что здесь:
- Request schemas (что принимаем от клиента)
- Response schemas (что отдаем клиенту)
- Валидация и сериализация данных

## Пример:
```python
# user.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    
    class Config:
        from_attributes = True  # для работы с ORM
```

## Правила:
- Разделяем Create/Update/Response схемы
- Используем Pydantic v2
- Строгая типизация всех полей