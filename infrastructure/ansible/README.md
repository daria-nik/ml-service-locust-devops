## Разворачивание сервиса с нуля с помощью Ansible

В проект включена минимальная инфраструктура как код (IaC), которая позволяет автоматически:
- устанавливать зависимости,
- собирать Docker-образ,
- запускать FastAPI-сервис в контейнере.

## Структура каталога

```
infrastructure/
└── ansible/
    ├── inventory.ini
    ├── playbook.yml
    └── roles/
        └── ml_service/
            └── tasks/
                └── main.yml
```

## 1. Настройка inventory

Файл `inventory.ini`:

```
[ml_service]
localhost ansible_connection=local
```

## 2. Основной playbook

Файл `playbook.yml`:

```yaml
- hosts: ml_service
  become: yes
  roles:
    - ml_service
```

## 3. Запуск Ansible

Убедитесь, что Ansible установлен:

```
pip install ansible
```

Запуск разворачивания сервиса:

```
ansible-playbook -i infrastructure/ansible/inventory.ini infrastructure/ansible/playbook.yml
```

## 4. Роль `ml_service`

Файл `roles/ml_service/tasks/main.yml`:

```yaml
---
- name: Build Docker image
  command: docker build -t ml-service ../../service/

- name: Run container
  command: docker run -d -p 8000:8000 ml-service
```

Роль выполняет:
1. Сборку Docker image из директории `service/`
2. Запуск контейнера на порту `8000`

## Итог

После выполнения команды:

```
ansible-playbook -i infrastructure/ansible/inventory.ini infrastructure/ansible/playbook.yml
```

На хосте автоматически развернется FastAPI-сервис, доступный по адресу:

```
http://localhost:8000/healthcheck
```
