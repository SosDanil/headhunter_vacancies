class Vacancy:
    def __init__(self, name: str, city: str, url: str, salary_from: int,
                 salary_to: int, requirement: str, responsibility: str):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, {self.salary_from}, {self.salary_to}, {self.city}, "
                f"{self.url}, {self.requirement}, {self.responsibility})")

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
        filtered_vacancies = []
        for vacancy in vacancies_list:
            for word in filter_word:
                if word in vacancy.name or word in vacancy.requirement or word in vacancy.responsibility:
                    filtered_vacancies.append(vacancy)
        return filtered_vacancies

    @staticmethod
    def get_sorted_vacancies(unsorted_vacancies: list) -> list:
        """Сортирует список, в нашем случае, объектов-вакансий по зарплате от большей к меньшей"""
        sorted_vacancies = sorted(unsorted_vacancies, reverse=True)
        return sorted_vacancies

    @classmethod
    def cast_to_object_list(cls, hh_vacancies: dict) -> list:
        vacancies_list = []
        for vacancy in hh_vacancies:
            name = vacancy["name"]
            city = vacancy["area"]["name"]
            url = vacancy["alternate_url"]

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
            responsibility = vacancy["snippet"]["responsibility"]
            if responsibility is None:
                responsibility = "не указано"

            vacancy_to_list = cls(name, city, url, salary_from, salary_to, requirement, responsibility)
            vacancies_list.append(vacancy_to_list)
        return vacancies_list



# if __name__ == '__main__':
#     test_vacancy = Vacancy("farmer", "Perm", "www.ru")
#     print(repr(test_vacancy))
#     print(test_vacancy)
