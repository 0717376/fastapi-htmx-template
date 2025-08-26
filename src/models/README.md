# Models

Модели данных для работы с базой данных (SQLAlchemy).

## Что здесь:
- ORM модели таблиц БД
- Relationships между таблицами
- Database mixins (created_at, updated_at)

## Пример:
```python
# user.py
from sqlalchemy import Column, String, Integer
from core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
```

## Правила:
- Один файл = одна модель (или связанная группа)
- Используем SQLAlchemy 2.0 синтаксис
- Никакой бизнес-логики, только структура данных