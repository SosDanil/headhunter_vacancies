class Vacancy:
    def __init__(self, name: str, city: str, url: str, requirement: str, responsibility: str, salary_from: int = 0,
                 salary_to: int = 0):
        self.name = name.lower()
        self.city = city.lower()
        self.url = url.lower()
        self.requirement = requirement.lower()
        self.responsibility = responsibility.lower()
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, {self.city}, {self.url}, {self.requirement}, "
                f"{self.responsibility}, {self.salary_from}, {self.salary_to})")

    def __str__(self):
        if self.salary_from == 0 and self.salary_to == 0:
            return (f"Профессия: {self.name}, зарплата не указана, "
                    f"в городе {self.city}, ссылка на сайт hh.ru: {self.url}\n"
                    f"Требования: {self.requirement}\n"
                    f"Обязанности: {self.responsibility}\n")
        elif self.salary_from == 0:
            return (f"Профессия: {self.name} с зарплатой до {self.salary_to} "
                    f"в городе {self.city}, ссылка на сайт hh.ru: {self.url}\n"
                    f"Требования: {self.requirement}\n"
                    f"Обязанности: {self.responsibility}\n")
        elif self.salary_to == 0:
            return (f"Профессия: {self.name} с зарплатой от {self.salary_from} "
                    f"в городе {self.city}, ссылка на сайт hh.ru: {self.url}\n"
                    f"Требования: {self.requirement}\n"
                    f"Обязанности: {self.responsibility}\n")
        else:
            return (f"Профессия: {self.name} с зарплатой от {self.salary_from} до {self.salary_to} "
                    f"в городе {self.city}, ссылка на сайт hh.ru: {self.url}\n"
                    f"Требования: {self.requirement}\n"
                    f"Обязанности: {self.responsibility}\n")

    def __lt__(self, other):
        # salary_from более важный показатель, чем salary_to (потому что может означать и от нуля)
        # итоговый результат сравнения объектов такой, какого я добивался
        if self.salary_from == 0 and other.salary_from == 0:
            if self.salary_to < other.salary_to:
                return True
            else:
                return False
        elif self.salary_to == 0 and other.salary_to == 0:
            if self.salary_from < other.salary_from:
                return True
            else:
                return False
        elif self.salary_from != 0 and other.salary_from == 0:
            return False
        elif self.salary_from == 0 and other.salary_from != 0:
            return True
        elif self.salary_from != 0 and other.salary_from != 0:
            if self.salary_from < other.salary_from:
                return True
            elif self.salary_from == other.salary_from:
                if self.salary_to < other.salary_to:
                    return True

    @staticmethod
    def get_filtered_vacancies(vacancies_list: list, filter_word: list) -> list:
        """Фильтрует список вакансий через заданные ключевые слова (если хотя бы одно совпадает)"""
        filtered_vacancies = []
        for vacancy in vacancies_list:
            for word in filter_word:
                if (word in vacancy.name or word in vacancy.city or word in vacancy.requirement or
                        word in vacancy.responsibility):
                    filtered_vacancies.append(vacancy)
        return filtered_vacancies

    @staticmethod
    def get_vacancies_by_salary(vacancies_list: list, salary_from: int, salary_to: int):
        """Сортирует список вакансий с учетом диапазона указанных зарплат"""
        vacancies_by_salary = []
        for vacancy in vacancies_list:
            if vacancy.salary_from == 0 and vacancy.salary_to == 0:
                continue
            elif salary_from <= vacancy.salary_from <= salary_to and salary_from <= vacancy.salary_to <= salary_to:
                vacancies_by_salary.append(vacancy)
            elif vacancy.salary_from == 0 and salary_from <= vacancy.salary_to <= salary_to:
                vacancies_by_salary.append(vacancy)
            elif vacancy.salary_to == 0 and salary_from <= vacancy.salary_from <= salary_to:
                vacancies_by_salary.append(vacancy)

        return vacancies_by_salary

    @staticmethod
    def get_sorted_vacancies(unsorted_vacancies: list) -> list:
        """Сортирует список, в нашем случае, объектов-вакансий по зарплате от большей к меньшей"""
        sorted_vacancies = sorted(unsorted_vacancies, reverse=True)
        return sorted_vacancies

    @staticmethod
    def get_top_vacancies(vacancies_list: list, top_number: int) -> list:
        """Формирует список из N позиций, в нашем случае, топ по зарплате"""
        return vacancies_list[0:top_number]

    @classmethod
    def cast_to_object_list(cls, hh_vacancies: list) -> list:
        """Создает список объектов-вакансий по словарю данных, полученных через api.hh.ru"""
        vacancies_list = []
        for vacancy in hh_vacancies:
            name = vacancy["name"].lower()
            city = vacancy["area"]["name"].lower()
            url = vacancy["alternate_url"].lower()

            try:
                salary_from = int(vacancy["salary"]["from"])
            except TypeError:
                salary_from = 0
            try:
                salary_to = int(vacancy["salary"]["to"])
            except TypeError:
                salary_to = 0

            requirement = vacancy["snippet"]["requirement"]
            if requirement is None:
                requirement = "не указано"
            else:
                requirement = requirement.lower()
            responsibility = vacancy["snippet"]["responsibility"]
            if responsibility is None:
                responsibility = "не указано"
            else:
                responsibility = responsibility.lower()

            vacancy_to_list = cls(name, city, url,  requirement, responsibility, salary_from, salary_to)
            vacancies_list.append(vacancy_to_list)
        return vacancies_list
