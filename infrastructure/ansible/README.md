Разворачивание сервиса с нуля с помощью Ansible

В проект включена минимальная инфраструктура как код (IaC), которая автоматически:

устанавливает зависимости,

разворачивает контейнер с FastAPI-сервисом,

обеспечивает воспроизводимый запуск.

Структура каталога:

infrastructure/
└── ansible/
├── inventory.ini
├── playbook.yml
└── roles/
└── ml_service/
└── tasks/
└── main.yml

Настройка inventory

Файл inventory.ini содержит список хостов:

[ml_service]
localhost ansible_connection=local

При необходимости можно заменить localhost на IP-адрес удалённого сервера.

Основной playbook

Файл playbook.yml:

hosts: ml_service
become: yes
roles:

ml_service

Запуск Ansible

Перед запуском убедитесь, что Ansible установлен:

pip install ansible

Запуск разворачивания сервиса:

ansible-playbook -i infrastructure/ansible/inventory.ini infrastructure/ansible/playbook.yml

Что делает роль ml_service

Файл roles/ml_service/tasks/main.yml выполняет:

установку Docker (если необходимо),

сборку Docker-образа,

запуск контейнера с ML-сервисом.

Содержимое main.yml:

name: Build Docker image
command: docker build -t ml-service ../../service/

name: Run container
command: docker run -d -p 8000:8000 ml-service

Итог

После выполнения команды:

ansible-playbook -i infrastructure/ansible/inventory.ini infrastructure/ansible/playbook.yml

На хосте автоматически разворачивается FastAPI-сервис, доступный по адресу:

http://localhost:8000/healthcheck
