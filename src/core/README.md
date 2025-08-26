# Core

Ядро приложения - конфигурация и базовые компоненты.

## Что здесь:
- `config.py` - настройки приложения (порты, БД, API keys)
- `database.py` - подключение к БД
- `security.py` - хеширование паролей, JWT токены
- `exceptions.py` - кастомные исключения

## Пример config.py:
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    database_url: str
    secret_key: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

## Правила:
- Все настройки через переменные окружения
- Никаких хардкод значений
- Один файл = одна ответственность