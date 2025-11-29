# Инструкция по развёртыванию

### 1. Сборка образа
docker build -t ml-service .

### 2. Запуск контейнера
docker run -p 8000:8000 ml-service

### 3. Проверка
http://localhost:8000/healthcheck
