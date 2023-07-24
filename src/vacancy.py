from src.json_saver import JsonSaver


class Vacancy(JsonSaver):
    """Класс для работы с вакансиями"""

    all = []

    def __init__(self, all_data, resource, name, city, url, date_time, salary_from, salary_to, currency, requirement):
        self.__all_data = all_data
        self.__resource = resource
        self.__name = name
        self.__city = city
        self.__url = url
        self.__date_time = date_time
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__currency = currency
        self.__requirement = requirement
        Vacancy.all.append(self)

    @property
    def all_data(self):
        return self.__all_data

    @property
    def resource(self):
        return self.__resource

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @property
    def url(self):
        return self.__url

    @property
    def date_time(self):
        return self.__date_time

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def currency(self):
        return self.__currency

    @property
    def requirement(self):
        return self.__requirement

    def creation_salary_string(self) -> str:
        """
        Создает корректную строку заработной платы исходя из того указана она или нет
        :return: f-строку заработной платы
        """
        salary_string = ""
        if self.salary_from and self.salary_to:
            salary_string = f"Зарплата от {self.salary_from} до {self.salary_to}"
        elif self.salary_from and not self.salary_to:
            salary_string = f"Зарплата от {self.salary_from}"
        elif self.salary_to and not self.salary_from:
            salary_string = f"Зарплата до {self.salary_to}"
        elif not self.salary_from and not self.salary_to:
            salary_string = "Зарплата не указана"
        if self.currency:
            salary_string += f" {self.currency}"
        return salary_string

    def __str__(self) -> str:
        """
        Создает информацию о вакансии для пользователя
        :return: f-строку с информацией о вакансии
        """
        return f"{self.name}\n{self.city}\n{self.creation_salary_string()}\n" \
               f"Требования: {self.requirement}\n" \
               f"Дата и время размещения: {self.date_time.strftime('%d.%m.%Y %H:%M:%S')}\n" \
               f"URL: {self.url}\n\n################################################################################\n"

    @classmethod
    def get_vacancies_by_salary_from(cls, vacancies: list, salary_from: int) -> list:
        """
        Получает список вакансий с зарплатой от указанной
        :param vacancies: список объектов класса Vacancy
        :param salary_from: сумма зарплаты
        :return: Список объектов класса Vacancy с зарплатой от указанной
        """
        vacancies_by_salary_from = []
        for vacancy in vacancies:
            if vacancy.salary_from:
                if vacancy.salary_from >= salary_from:
                    vacancies_by_salary_from.append(vacancy)
        return vacancies_by_salary_from

    @classmethod
    def get_vacancies_by_salary_to(cls, vacancies: list, salary_to: int) -> list:
        """
        Получает список вакансий с зарплатой до указанной
        :param vacancies: список объектов класса Vacancy
        :param salary_to: сумма зарплаты
        :return: Список объектов класса Vacancy с зарплатой до указанной
        """
        vacancies_by_salary_to = []
        for vacancy in vacancies:
            if vacancy.salary_to:
                if vacancy.salary_to <= salary_to:
                    vacancies_by_salary_to.append(vacancy)
        return vacancies_by_salary_to

    @classmethod
    def sort_by_salary(cls, vacancies):
        """
        Сортирует вакансии по зарплате
        :param vacancies: список объектов класса Vacancy
        :return: словарь с двумя списками вакансий отсортированных по зарплате в прямом и обратном порядке
        """
        objects_for_sort = {}
        ascending = []
        descending = []
        for vacancy in vacancies:
            if vacancy.salary_from:
                objects_for_sort[vacancy.salary_from] = vacancy
        objects_sorted = dict(sorted(objects_for_sort.items()))
        for value in objects_sorted.values():
            ascending.append(value)
        objects_sorted_reverse = dict(sorted(objects_for_sort.items(), reverse=True))
        for value in objects_sorted_reverse.values():
            descending.append(value)
        sorted_dict = {}
        sorted_dict['ascending'] = ascending
        sorted_dict['descending'] = descending
        return sorted_dict

    @classmethod
    def sort_by_date(cls, vacancies):
        """
        Сортирует вакансии по дате
        :param vacancies: список объектов класса Vacancy
        :return: словарь с двумя списками вакансий отсортированных по дате в прямом и обратном порядке
        """
        objects_for_sort = {}
        ascending = []
        descending = []
        for vacancy in vacancies:
            if vacancy.date_time:
                objects_for_sort[vacancy.date_time] = vacancy
        objects_sorted = dict(sorted(objects_for_sort.items()))
        for value in objects_sorted.values():
            ascending.append(value)
        objects_sorted_reverse = dict(sorted(objects_for_sort.items(), reverse=True))
        for value in objects_sorted_reverse.values():
            descending.append(value)
        sorted_dict = {}
        sorted_dict['ascending'] = ascending
        sorted_dict['descending'] = descending
        return sorted_dict