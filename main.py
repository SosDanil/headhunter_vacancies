from src.API import HeadHunterAPI
from src.Vacancy import Vacancy


def main():
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_response("парикмахер")
    Vacancy.cast_to_object_list(hh_vacancies)
    for vacancy in Vacancy.vacancies_list:
        print(vacancy)

main()