# Используем официальный минимальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . .

# Открываем порт 5000 для Flask
EXPOSE 5000

# Запускаем приложение
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
