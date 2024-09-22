from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.getenv('GITHUB_TOKEN')
USERNAME = os.getenv('GITHUB_USERNAME')

print(USERNAME)

''' ��ункция для получения заголовков с токеном авторизации '''


def get_headers(TOKEN):
    return {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }


''' Функция для создания репозитория '''


def create_github_repo(token, repo_name, private=True):
    url = "https://api.github.com/user/repos"
    payload = {
        "name": repo_name,
        "private": private
    }

    response = requests.post(url, json=payload, headers=get_headers(token))

    if response.status_code == 201:
        print(f"Репозиторий '{repo_name}' успешно создан.")
        return True
    else:
        print(f"Не удалось создать репозиторий. Ошибка: {response.status_code}")
        print(response.json())
        return False


''' Функция для просмотра существующих репозиториев '''


def list_github_repos(TOKEN):
    repos = []
    page = 1
    per_page = 100

    while True:
        url = f"https://api.github.com/user/repos?type=all&per_page={per_page}&page={page}"
        response = requests.get(url, headers=get_headers(TOKEN))

        if response.status_code == 200:
            page_repos = response.json()
            if not page_repos:
                break
            repos.extend(page_repos)
            page += 1
        else:
            print(f"Не удалось получить список репозиториев. Ошибка: {response.status_code}")
            print(response.json())
            break

    if repos:
        print("Список ваших репозиториев:")
        for repo in repos:
            print(f"- {repo['name']}")
        print('Всего репозиториев:', len(repos))
    else:
        print("У вас нет репозиториев.")


''' Функция для удаления репозитория '''


def delete_github_repo(TOKEN, repo_name):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"

    response = requests.delete(url, headers=get_headers(TOKEN))

    if response.status_code == 204:
        print(f"Репозиторий '{repo_name}' успешно удалён.")
    else:
        print(f"Не удалось удалить репозиторий. Ошибка: {response.status_code}")
        print(response.json())


''' Меню консоли '''


def github_menu():

    while True:
        print("\nВыберите действие:")
        print("1 - Создать новый репозиторий")
        print("2 - Просмотреть существующие репозитории")
        print("3 - Удалить репозиторий")
        print("0 - Выйти")

        choice = input("\nВаш выбор: ")

        if choice == "1":
            repo_name = input("Введите название нового репозитория: ")
            private = input("Приватный репозиторий? (y/n): ").lower() == 'y'
            create_github_repo(TOKEN, repo_name, private)

        elif choice == "2":
            list_github_repos(TOKEN)

        elif choice == "3":
            repo_name = input("Введите название репозитория для удаления: ")
            delete_github_repo(TOKEN, repo_name)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    github_menu()
