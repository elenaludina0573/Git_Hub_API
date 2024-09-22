# E2E UI тест для SauceDemo

В данном проекте реализована возможность управлять репозиториями Github с помощью терминала python. 

# Структура проекта

- test_api.py: Основной скрипт, содержащий сценарий проекта.
- .venv/: Виртуальное окружение для управления зависимостями (не включено в репозиторий).
- README.md: Документация по настройке и запуску проекта.

# Инструкции по настройке

# 1. Клонируйте репозиторий

```
git clone https://github.com/elenaludina0573/Git_Hub_API
cd <директория_проекта>
```
# 2. Где взять API

Для того чтобы получить API, необходимо перейти в настройки вашего аккаунта github settings-> developer settings 
-> Personal access tokens (classic) -> генерируйте новый токен, проставить галочки можно везде.

# 3. Виртуальное окружение
## На Windows
```
python -m venv venv
venv\Scripts\activate
```
## На macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

# 4. Зависимости
Можно через requirements.txt
```
pip install -r requirements.txt
```
Или вручную 
```
pip install requests
pip instell python-dotenv
  
selenium  install
python-dotenv install

```
# 5. Запуск
```
python test_api.py
```

# Использование GitHub API:
## Скрипт должен использовать API GitHub для выполнения следующих операций:
   1. Создание нового публичного репозитория.
   2. Проверка списка репозиториев для подтверждения создания.
   3. Удаление репозитория.
