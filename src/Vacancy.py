class Vacancy:
    vacancies_list = []

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
                f"{self.url})")

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

    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
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
            try:
                requirement = vacancy["snippet"]["requirement"]
            except TypeError:
                requirement = "не указано"
            try:
                responsibility = vacancy["snippet"]["responsibility"]
            except TypeError:
                responsibility = "не указано"

            vacancy_to_list = cls(name, city, url, salary_from, salary_to, requirement, responsibility)
            cls.vacancies_list.append(vacancy_to_list)




# if __name__ == '__main__':
#     test_vacancy = Vacancy("farmer", "Perm", "www.ru")
#     print(repr(test_vacancy))
#     print(test_vacancy)
