class Vacancy:
    def __init__(self, name: str, salary_from: int, salary_to: int, city: str, url: str):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city
        self.url = url

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, {self.salary_from}, {self.salary_to}, {self.city},"
                f" {self.url})")


if __name__ == '__main__':
    test_vacancy = Vacancy('farmer', 30000, 50000, "Perm", "www.ru")
    print(repr(test_vacancy))