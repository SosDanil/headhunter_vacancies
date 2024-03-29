import json
from abc import ABC, abstractmethod


class FileManager(ABC):
    @abstractmethod
    def add_to_file(self, path, vacancies):
        pass

    @abstractmethod
    def read_file(self, path):
        pass

    @abstractmethod
    def delete_from_file(self, path):
        pass


class JSONManager(FileManager):
    def __init__(self):
        pass

    def add_to_file(self, path, vacancies):
        """Записывает данные о вакансиях в файл в формате json"""
        vacancies_list = []
        for vacancy in vacancies:
            json_vacancy = {"Название вакансии": vacancy.name, "Город": vacancy.city, "Ссылка": vacancy.url,
                            "Зарплата от": vacancy.salary_from, "Зарплата до": vacancy.salary_to,
                            "Требования": vacancy.requirement, "Обязанности": vacancy.responsibility}
            vacancies_list.append(json_vacancy)
        with open(path, 'w', encoding="UTF-8") as f:
            json.dump(vacancies_list, f, indent=4, ensure_ascii=False)

    def read_file(self, path):
        """Выводит информацию из файла"""
        with open(path, "r", encoding="UTF-8") as f:
            data = json.load(f)
        print(json.dumps(data, indent=4,  ensure_ascii=False))

    def delete_from_file(self, path):
        """Очищает файл и оставляет там пустой список"""
        empty_list = []
        with open(path, "w", encoding="UTF-8") as f:
            json.dump(empty_list, f)
