class Vacancy:
    vacancies_list = []

    def __init__(self, name: str, city: str, url: str, salary_from: int = 0,
                 salary_to: int = 0):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city
        self.url = url

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, {self.salary_from}, {self.salary_to}, {self.city}, "
                f"{self.url})")

    def __str__(self):
        return (f"Профессия: {self.name} с зарплатой от {self.salary_from} до {self.salary_to} "
                f"в городе {self.city}, ссылка на сайт hh.ru: {self.url}")

    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
        for vacancy in hh_vacancies:
            name = vacancy["name"]
            city = vacancy["area"]["name"]
            url = vacancy["alternate_url"]
            salary_from = vacancy["salary"]["from"]
            salary_to = vacancy["salary"]["to"]
            vacancy_to_list = cls(name, city, url, salary_from, salary_to)
            cls.vacancies_list.append(vacancy_to_list)



# if __name__ == '__main__':
#     test_vacancy = Vacancy("farmer", "Perm", "www.ru")
#     print(repr(test_vacancy))
#     print(test_vacancy)
