from src.saver import Saver
import json


class JsonSaver(Saver):
    """Класс для работы с json-файлом"""

    @classmethod
    def save_to_file(cls, vacancies: list) -> None:
        """
        Преобразует полученный список объектов в список данных о вакансиях в json-формате
        и сохраняет его в json-файл
        :param vacancies: список объектов класса Vacancy
        """
        save_list = []
        for vacancy in vacancies:
            save_list.append(vacancy.all_data)
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(save_list, file, ensure_ascii=False)

    @classmethod
    def read_from_file(cls) -> list:
        """
        Получает данные о вакансиях из json-файла
        """
        with open('vacancies.json', 'r') as file:
            text = json.load(file)
            return text

    @classmethod
    def clear_file(cls) -> None:
        """
        Удаляет все данные из json-файла
        """
        with open('vacancies.json', 'w') as file:
            pass