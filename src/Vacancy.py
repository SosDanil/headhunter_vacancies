class Vacancy:
    def __init__(self, name: str, city: str, url: str, salary_from: int = "'не указано'",
                 salary_to: int = "'не указано'"):
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


# if __name__ == '__main__':
#     test_vacancy = Vacancy("farmer", "Perm", "www.ru")
#     print(repr(test_vacancy))
#     print(test_vacancy)
