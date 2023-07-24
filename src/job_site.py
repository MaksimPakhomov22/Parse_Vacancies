from abc import ABC, abstractmethod


class JobSite(ABC):
    """Абстрактный класс для назначения конкретных платформ с вакансиями"""

    @abstractmethod
    def get_vacancies_list(self):
        """
        Обязывает дочерние классы реализовать метод получения вакансий по API
        """
        pass

    @abstractmethod
    def creation_objects(self, response):
        """
        Обязывает дочерние классы реализовать метод создания списка объектов класса Vacancy
        из списка полученного по API
        """
        pass
