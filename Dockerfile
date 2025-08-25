# Используем официальный Python образ как базовый
FROM python:3.12-slim

# Устанавливаем uv
# COPY_BUFSIZE=65536 ускоряет копирование больших файлов
ENV COPY_BUFSIZE=65536
RUN pip install uv

# Создаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
# Сначала копируем только файлы с зависимостями для кэширования слоев
COPY pyproject.toml ./
COPY uv.lock* ./

# Устанавливаем зависимости через uv
RUN uv sync --frozen --no-install-project

# Копируем остальной код приложения
COPY . .

# Устанавливаем сам проект
RUN uv sync --frozen

# Запускаем приложение через uv
CMD ["uv", "run", "python", "src/main.py"]