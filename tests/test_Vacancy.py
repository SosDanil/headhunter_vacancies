import pytest
from src.Vacancy import Vacancy

test_vacancy1 = Vacancy("Механик",
                        "Пермь",
                        "www.hh.ru/vacancies/234561",
                        "Опыт 1-3 года, ответственность, скиллы мастера,",
                        "Чинить сломанное, уважать клиентов",
                        50000, 100000)

test_vacancy2 = Vacancy("Стилист",
                        "Москва",
                        "www.hh.ru/vacancies/234562",
                        "Без опыта, ответственность, свои инструменты",
                        "Делать людей красивыми",
                        salary_to=150000)

test_vacancy3 = Vacancy("Бортпроводник",
                        "Екатеринбург",
                        "www.hh.ru/vacancies/234563",
                        "отсутствие страха полетов",
                        "Разность еду, поддерживать пассажиров",
                        70000, 170000)

test_vacancy4 = Vacancy("Повар в столовой",
                        "Пермь",
                        "www.hh.ru/vacancies/234564",
                        "Опыт работы в школьной столовой,"
                        "опрятность, соблюдение гигиены, скиллы мастера",
                        "Делать людям вкусно и приятно на душе",
                        20000)

test_vacancy5 = Vacancy("Дворник",
                        "Екатеринбург",
                        "www.hh.ru/vacancies/234565",
                        "без опыта, иметь свою метлу пунктуальность",
                        "Мастерски подметать дворы")

test_vacancy6 = Vacancy("Лаборант",
                        "Москва",
                        "www.hh.ru/vacancies/234567",
                        "Высшее образование, ответственность, тяга к науке",
                        "помогать в выполнении научных задач основному персоналу",
                        20000, 30000)

# тестовый список вакансий, полученый через hh.api
test_hh_vacancies = [
    {
        "name": "Охранник",
        "area": {"name": "Самара"},
        "alternate_url": "www.hh.api.cat",
        "salary": {"from": "30000", "to": "50000"},
        "snippet": {"requirement": "Умение стрелять", "responsibility": None}
    },
    {
        "name": "Уборщица",
        "area": {"name": "Иркутск"},
        "alternate_url": "www.hh.api.dog",
        "salary": {"from": None, "to": None},
        "snippet": {"requirement": None, "responsibility": "Мыть полы"}
    }
]


@pytest.fixture
def vacancies_list():
    vacancies_list = [test_vacancy1, test_vacancy2, test_vacancy3, test_vacancy4, test_vacancy5, test_vacancy6]
    return vacancies_list


def test_get_filtered_vacancies(vacancies_list):
    # слова для фильтрации в основной программе будут приходить в малом регистре
    assert Vacancy.get_filtered_vacancies(vacancies_list, ["опыт"]) == [test_vacancy1, test_vacancy2,
                                                                        test_vacancy4, test_vacancy5]
    assert Vacancy.get_filtered_vacancies(vacancies_list, ["пермь"]) == [test_vacancy1, test_vacancy4]
    assert Vacancy.get_filtered_vacancies(vacancies_list, ["пермь", "дворник"]) == [test_vacancy1,
                                                                                    test_vacancy4, test_vacancy5]
    assert Vacancy.get_filtered_vacancies(vacancies_list, ["ответственность"]) == [test_vacancy1,
                                                                                   test_vacancy2, test_vacancy6]
    assert Vacancy.get_filtered_vacancies(vacancies_list, ["механик", "стилист", "повар", "дворник",
                                                           "лаборант", "проводник"]) == [test_vacancy1, test_vacancy2,
                                                                                         test_vacancy3, test_vacancy4,
                                                                                         test_vacancy5, test_vacancy6]
    assert Vacancy.get_filtered_vacancies(vacancies_list, ["котик"]) == []


def test_get_vacancies_by_salary(vacancies_list):
    assert Vacancy.get_vacancies_by_salary(vacancies_list, 50000, 80000) == []
    assert Vacancy.get_vacancies_by_salary(vacancies_list, 0, 0) == []
    assert Vacancy.get_vacancies_by_salary(vacancies_list, 10000, 200000) == [test_vacancy1,
                                                                              test_vacancy2, test_vacancy3,
                                                                              test_vacancy4, test_vacancy6]
    assert Vacancy.get_vacancies_by_salary(vacancies_list, 0, 50000) == [test_vacancy4,
                                                                         test_vacancy6]


def test_get_sorted_vacancies(vacancies_list):
    assert Vacancy.get_sorted_vacancies(vacancies_list) == [test_vacancy3, test_vacancy1, test_vacancy6,
                                                            test_vacancy4, test_vacancy2, test_vacancy5]


def test_get_top_vacancies(vacancies_list):
    # в данном тесте получает не отсортированный список, но не суть, главное функционал
    assert Vacancy.get_top_vacancies(vacancies_list, 3) == [test_vacancy1, test_vacancy2, test_vacancy3]
    assert Vacancy.get_top_vacancies(vacancies_list, 0) == []
    assert Vacancy.get_top_vacancies(vacancies_list, 10) == [test_vacancy1, test_vacancy2, test_vacancy3,
                                                             test_vacancy4, test_vacancy5, test_vacancy6]


# def test_cast_to_object_list():
#     assert Vacancy.cast_to_object_list(test_hh_vacancies) == [
#         Vacancy("охранник", "самара", "www.hh.api.cat", "умение стрелять", "не указано", 30000, 50000),
#         Vacancy("уборщица", "иркутск", "www.hh.api.dog", "не указано", "мыть полы", 0, 0)]
