ML-Service + Locust Load Testing + ADR + IaC
Репозиторий итогового DevOps задания

Этот проект представляет собой воспроизводимый ML-сервис, разворачиваемый с нуля через Docker, покрытый нагрузочным тестированием Locust и сопровождаемый архитектурной документацией ADR.
Работа выполнена по методологии API-first, включает описание архитектуры, анализ альтернативных решений, инфраструктуру, скрипты тестирования и результаты исследования дрейфа данных.

1. Структура проекта
ml-service-locust-devops/
│
├── service/
│   └── main.py                 # FastAPI ML-сервис
│
├── load_tests/
│   ├── locustfile.py           # Нагрузочные тесты Locust
│   └── report.html             # Отчёт тестирования
│
├── adr_records/
│   ├── index.md
│   └── 0001-why-we-chose-this-architecture.md
│
├── infrastructure/
│   ├── Dockerfile              # Разворачивание сервиса
│   └── README.md               # Инструкция запуска контейнера
│
├── notebooks/
│   └── mlflow_evidently_drift.ipynb  # Анализ drift данных
│
├── requirements.txt
└── README.md

2. API-first архитектура

Проект построен по принципу API-first:

Эндпоинты сервиса
Метод	Путь	Назначение
GET	/healthcheck	Проверяет доступность сервиса
POST	/predict	Возвращает простое ML-предсказание (демо)

API описан в service/main.py и может быть запущен через Docker или напрямую в Colab.

3. ADR — Архитектурные решения

Проект содержит архитектурный документ ADR:

adr_records/0001-why-we-chose-this-architecture.md

Документ содержит:

описание проблемы

анализ двух вариантов: монолит vs микросервис

принятие решения

последствия

компромиссы


4. Инфраструктура (IaC)

Сервис полностью воспроизводим с нуля благодаря Docker.

Сборка
docker build -t ml-service .

Запуск
docker run -p 8000:8000 ml-service

Проверка
http://localhost:8000/healthcheck


Dockerfile лежит в infrastructure/Dockerfile.

5. ML-компонент и анализ дрейфа данных

В проект включено:

- вычисление простого предсказания
- демонстрационный анализ дрейфа данных через Evidently
- MLFlow для воспроизводимости

Все шаги описаны в ноутбуке:

notebooks/mlflow_evidently_drift.ipynb


6. Нагрузочное тестирование Locust

Нагрузочные тесты расположены в load_tests/locustfile.py.

Запуск тестов
locust -f load_tests/locustfile.py --headless \
       -u 10 -r 1 --run-time 30s \
       --host http://0.0.0.0:8000 \
       --html load_tests/report.html

Результаты

Полный отчёт: load_tests/report.html

Основные наблюдения:

сервис выдерживает плавный рост нагрузки

количество ошибок 0

RPS стабилен

медианная задержка низкая

деградации на пике не наблюдается

Эти данные входят в критерий нагрузочного тестирования + выводы.
