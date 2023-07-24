from src.vacancy import Vacancy
from src.utils import get_vacancies_by_api, get_vacancies_from_file, get_vacancies_by_salary, printing_vacancies,\
    creation_salary_dict

get_vacancies_by_api()

vacancies = get_vacancies_from_file()
printing_vacancies(vacancies)

request = None
while True:
    user_answer = input("\nВыберите действие со списком:\n"
                        "1 - Сортировать по заработной плате от и до\n"
                        "2 - Сортировать по возрастанию зарплаты\n"
                        "3 - Сортировать по убыванию зарплаты\n"
                        "4 - Сортировать по дате, свежие сверху\n"
                        "5 - Сортировать по дате, свежие снизу\n"
                        "6 - Сбросить фильтр\n"
                        "7 - Обновить список\n"
                        "8 - Удалить все данные из файла\n"
                        "0 - Выход\n")
    if not user_answer.isdigit():
        print("Не верный ввод! Должна быть цифра!\n")
    elif int(user_answer) not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print("Не верный ввод! Введите цифру от 0 до 8\n")
    elif int(user_answer) == 0:
        print("До скорого!!!")
        break
    else:
        request = int(user_answer)
        if request == 1:
            salary = creation_salary_dict(vacancies)
            get_vacancies_by_salary(salary)
            printing_vacancies(get_vacancies_from_file())
        elif request == 2:
            Vacancy.save_to_file(Vacancy.sort_by_salary(vacancies)['ascending'])
            printing_vacancies(get_vacancies_from_file())
        elif request == 3:
            Vacancy.save_to_file(Vacancy.sort_by_salary(vacancies)['descending'])
            printing_vacancies(get_vacancies_from_file())
        elif request == 4:
            Vacancy.save_to_file(Vacancy.sort_by_date(vacancies)['descending'])
            printing_vacancies(get_vacancies_from_file())
        elif request == 5:
            Vacancy.save_to_file(Vacancy.sort_by_date(vacancies)['ascending'])
            printing_vacancies(get_vacancies_from_file())
        elif request == 6:
            Vacancy.save_to_file(vacancies)
            printing_vacancies(vacancies)
        elif request == 7:
            get_vacancies_by_api()
            vacancies = get_vacancies_from_file()
            printing_vacancies(vacancies)
        elif request == 8:
            Vacancy.clear_file()
            print("\nФайл очищен\n_________________________________________")
