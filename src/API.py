from abc import ABC, abstractmethod

import requests


class BaseAPI(ABC):
    @abstractmethod
    def get_response(self, vacancy_name):
        pass


class HeadHunterAPI(BaseAPI):

    def get_response(self, vacancy_name):
        params = {
            "text": f"NAME:{vacancy_name}",
            "page": 0,
            "per_page": 100
        }
        response = requests.get(f"https://api.hh.ru/vacancies/", params=params)
        return response


# if __name__ == '__main__':
#     hh_api = HeadHunterAPI()
#     hh_response = hh_api.get_response("парикмахер")
#     print(hh_response)
#     print(hh_response.status_code)
#     print(hh_response.ok)
#     print(hh_response.json())



