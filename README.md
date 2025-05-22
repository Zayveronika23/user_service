# Сервис для хранения пользователей.           

### Краткое описание:
Сервис для хранения пользователей

### Сборка и запуск:

```bash
Клонируем репозиторий 
git clone git@github.com:Zayveronika23/user_service.git

Переходим в директорию:
cd user_service

Cоздаем и активируем виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

Устанавливаем необходимые зависимости
pip install -r requirements.txt

Запускаем проект:
uvicorn app.main:app --reload
```
### Примеры запросов:
* GET запрос к /users/{user_id} - для получения конкретного пользователя

* PUT запрос к /users/{user_id} - для изменения данных пользователя

* DELETE запрос к /users/{user_id} - для удаления пользователя

* GET запрос к /users - для получения списка всех пользователей

* POST запрос к /users - для создания нового пользователя

