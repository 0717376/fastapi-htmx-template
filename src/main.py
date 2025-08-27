from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Создаем FastAPI приложение с названием для документации
app = FastAPI(title="FastAPI + HTMX Template")

# Получаем путь к текущей папке src/
BASE_DIR = Path(__file__).resolve().parent

# Подключаем папку static/ - все файлы оттуда доступны по URL /static/...
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Подключаем папку templates/ для HTML шаблонов
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)  # Главная страница возвращает HTML
async def home(request: Request):
    # Рендерим шаблон и передаем в него данные
    return templates.TemplateResponse(
        "pages/index.html",  # Путь к шаблону
        {"request": request, "title": "FastAPI + HTMX"}  # Данные для шаблона
    )


@app.get("/daisyui", response_class=HTMLResponse)  # Страница с компонентами DaisyUI
async def daisyui_components(request: Request):
    return templates.TemplateResponse(
        "pages/daisyui.html",
        {"request": request, "title": "DaisyUI Components"}
    )


@app.get("/preline", response_class=HTMLResponse)  # Страница с компонентами Preline UI
async def preline_components(request: Request):
    return templates.TemplateResponse(
        "pages/preline.html",
        {"request": request, "title": "Preline UI Components"}
    )


@app.get("/custom", response_class=HTMLResponse)  # Страница с кастомными компонентами
async def custom_components(request: Request):
    return templates.TemplateResponse(
        "pages/custom.html",
        {"request": request, "title": "Custom UI Components"}
    )


@app.get("/apple", response_class=HTMLResponse)  # Страница в стиле Apple
async def apple_components(request: Request):
    return templates.TemplateResponse(
        "pages/apple.html",
        {"request": request, "title": "Apple Style UI"}
    )


@app.get("/api/hello")  # API endpoint возвращает JSON
async def hello():
    return {"message": "Hello from FastAPI!"}