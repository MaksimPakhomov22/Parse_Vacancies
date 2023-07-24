from src.job_site import JobSite
import requests
from src.vacancy import Vacancy
from datetime import datetime


class HeadHunter(JobSite):
    """Класс для работы с платформой HeadHunter"""

    def __init__(self, params):
        self.url = "https://api.hh.ru/vacancies"
        self.params = params
        self.vacancies_list = []

    def get_vacancies_list(self) -> list:
        """
        Получает вакансии по API
        :return: список вакансий в формате json
        """
        while self.params['page'] > 0:
            response = requests.get(self.url, params=self.params).json()['items']
            for vacancy in response:
                vacancy['resource'] = 'HeadHunter'
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
            name = vacancy['name']
            city = vacancy['area']['name']
            url = vacancy['apply_alternate_url']
            published_at = vacancy['published_at'].split('+')[0]
            date_time = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S')
            if vacancy['salary']:
                salary_from = vacancy['salary']['from']
                salary_to = vacancy['salary']['to']
                currency = vacancy['salary']['currency']
            else:
                salary_from = None
                salary_to = None
                currency = None
            if vacancy['snippet']['requirement']:
                requirement = vacancy['snippet']['requirement']
            else:
                requirement = "Не указаны"
            vac_object = Vacancy(all_data, resource, name, city, url, date_time,
                                 salary_from, salary_to, currency, requirement)
            objects_vacancy.append(vac_object)
        return objects_vacancy