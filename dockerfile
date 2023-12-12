FROM python:3.9

# Установка переменной окружения для отключения вывода виртуального окружения Python
ENV PYTHONUNBUFFERED 1

# Создание и установка рабочей директории внутри образа
WORKDIR /app

# Копирование зависимостей проекта в образ
COPY requirements.txt /app/

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование файлов проекта в образ
COPY . /app/

# Установка supervisord
RUN apt-get update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*

# Копирование конфигурационного файла supervisord
COPY supervisord.conf /etc/supervisor/conf.d/

# Запуск supervisord, который будет запускать uvicorn
CMD ["/usr/bin/supervisord", "-n"]