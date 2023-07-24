from abc import ABC, abstractmethod
import json


class Saver(ABC):

    @abstractmethod
    def save_to_file(self, vacancies):
        pass

    @abstractmethod
    def read_from_file(self):
        pass

    @abstractmethod
    def clear_file(self):
        pass


class JsonSaver(Saver):
    @classmethod
    def save_to_file(cls, vacancies: list) -> None:
        save_list = []
        for vacancy in vacancies:
            save_list.append(vacancy.all_data)
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(save_list, file, ensure_ascii=False)

    @classmethod
    def read_from_file(cls) -> list:
        with open('vacancies.json', 'r') as file:
            text = json.load(file)
            return text

    @classmethod
    def clear_file(cls) -> None:
        with open('vacancies.json', 'w') as file:
            pass
