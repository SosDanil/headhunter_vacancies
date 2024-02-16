from src.API import HeadHunterAPI
from src.Vacancy import Vacancy
from src.FileManager import JSONManager
from config import PATH_TO_JSON_DATA


def main():
    print("Здравствуйте! Как здорово, что вы решились на поиск работы, мы готовы вам помочь!")
    while True:
        search_query = input("Введите поисковый запрос (название вакансии):  ")
        filter_words = input("Введите ключевые слова через запятую (город, требования, обязанности):  ").lower().split(", ")

        while True:
            try:
                salary_from = int(input("Введите нижний порог зарплаты:  "))
                break
            except ValueError:
                print("Попробуйте снова, введите число")
                continue

        while True:
            try:
                salary_to = int(input("Введите верхний порог зарплаты:  "))
                break
            except ValueError:
                print("Попробуйте снова, введите число")
                continue

        while True:
            try:
                top_number = int(input("Введите число - топ N вакансий, которые хотите увидеть:  "))
                break
            except ValueError:
                print("Попробуйте снова, введите число")
                continue

        hh_api = HeadHunterAPI()
        hh_vacancies = hh_api.get_vacancies(search_query)
        vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
        filtered_vacancies = Vacancy.get_filtered_vacancies(vacancies_list, filter_words)
        sorted_vacancies = Vacancy.get_sorted_vacancies(filtered_vacancies)
        vacancies_by_salary = Vacancy.get_vacancies_by_salary(sorted_vacancies, salary_from, salary_to)
        top_vacancies = Vacancy.get_top_vacancies(vacancies_by_salary, top_number)

        json_saver = JSONManager()
        json_saver.add_to_file(PATH_TO_JSON_DATA, top_vacancies)
        print("Ниже список вакансий, что вы искали")
        json_saver.read_file(PATH_TO_JSON_DATA)
        print("Найденные вакансии сохранены в файл")
        user_final_input = int(input("Если хотите повторить запрос, введите '1', если хотите закончить, введите '2': "))
        if user_final_input == 1:
            continue
        elif user_final_input == 2:
            break
    print("Спасибо, что воспользовались нашими услугами!")


main()
