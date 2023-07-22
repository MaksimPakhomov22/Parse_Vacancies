from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def save_to_file(self, vacancies):
        """
        Обязывает дочерние классы реализовать метод сохранения данных в файл
        """
        pass

    @abstractmethod
    def read_from_file(self):
        """
        Обязывает дочерние классы реализовать метод получения данных из файла
        """
        pass

    @abstractmethod
    def clear_file(self):
        """
        Обязывает дочерние классы реализовать метод удаления данных из файла
        """
        pass