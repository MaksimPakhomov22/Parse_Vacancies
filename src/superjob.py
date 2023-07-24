from src.job_site import JobSite
import os
import requests
from src.vacancy import Vacancy
from datetime import datetime


class SuperJob(JobSite):
    """Класс для работы с платформой SuperJob"""

    def __init__(self, params):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.api_key = os.getenv('SUPERJOB_API_KEY')
        self.headers = {'X-Api-App-Id': self.api_key}
        self.params = params
        self.vacancies_list = []

    def get_vacancies_list(self) -> list:
        """
        Получает вакансии по API
        :return: список вакансий в формате json
        """
        while self.params['page'] > 0:
            response = requests.get(self.url, headers=self.headers, params=self.params).json()['objects']
            for vacancy in response:
                vacancy['resource'] = 'SuperJob'
                self.vacancies_list.append(vacancy)
            self.params['page'] -= 1
        return self.vacancies_list

    @classmethod
    def creation_objects(cls, vacancies: list) -> list:
        """
        Преобразует список вакансий полученный по API в список объектов класса Vacancy
        :param vacancies: список вакансий в формате json
        :return: список объектов класса Vacancy
        """
        objects_vacancy = []
        for vacancy in vacancies:
            all_data = vacancy
            resource = vacancy['resource']
            name = vacancy['profession']
            city = vacancy['town']['title']
            url = vacancy['link']
            date_time = datetime.fromtimestamp(vacancy['date_published'])
            salary_from = vacancy['payment_from']
            salary_to = vacancy['payment_to']
            currency = vacancy['currency']
            requirement = vacancy['candidat']
            vac_object = Vacancy(all_data, resource, name, city, url, date_time,
                                 salary_from, salary_to, currency, requirement)
            objects_vacancy.append(vac_object)
        return objects_vacancy