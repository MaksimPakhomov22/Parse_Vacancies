from src.hh import HeadHunter
from src.superjob import SuperJob
from src.vacancy import Vacancy


def get_vacancies_by_api() -> None:
    """
    Устанавливает параметры для запроса по API, получает вакансии со всех платформ, объединяет их в общий список
    и сохраняет его в json-файл
    """
    keyword = input("Введите название профессии или слово для поиска вакансии.\n"
                    "Если хотите вызвать весь список, то нажмите ENTER: ")
    print("Просьба ожидать, идет формирование списка вакансий")
    # По умолчанию установлены максимальные значения количества вакансий на странице ('per_page' и 'count')
    # и количества страниц для запроса ('page')
    params_hh = {'per_page': 100, 'page': 19, 'text': keyword}
    params_sj = {'count': 100, 'page': 5, 'not_archive': True, 'keyword': keyword}
    vac_hh = HeadHunter(params_hh)
    vac_sj = SuperJob(params_sj)
    vac_list_hh = vac_hh.get_vacancies_list()
    vac_list_sj = vac_sj.get_vacancies_list()
    hh_init_list = HeadHunter.creation_objects(vac_list_hh)
    sj_init_list = SuperJob.creation_objects(vac_list_sj)
    common_list = hh_init_list + sj_init_list
    Vacancy.save_to_file(common_list)


def get_vacancies_from_file() -> list:
    """
    Получает вакансии из json-файла, преобразует из в списки объектов класса Vacancy и объединяет в общий список
    :return: список объектов класса Vacancy
    """
    hh_list_for_init = []
    sj_list_for_init = []
    for vac in Vacancy.read_from_file():
        if vac['resource'] == 'HeadHunter':
            hh_list_for_init.append(vac)
        elif vac['resource'] == 'SuperJob':
            sj_list_for_init.append(vac)
    hh_init_list = HeadHunter.creation_objects(hh_list_for_init)
    sj_init_list = SuperJob.creation_objects(sj_list_for_init)
    return hh_init_list + sj_init_list


def creation_salary_dict(vacancies) -> dict:
    """
    Запрашивает у пользователя суммы зарплаты от и до, и формирует словарь с этими параметрами.
    По умолчанию параметры None
    :return: словарь с параметрами зарплаты от и до
    """
    salary = {'from': None, 'to': None}
    request = True
    while True:
        salary_from = input("Введите сумму зарплаты от, если не важно, нажмите ENTER,\n"
                            "для возврата к предыдущему меню введите EXIT:  ")
        if salary_from.lower() == 'exit':
            request = False
            Vacancy.save_to_file(vacancies)
            break
        elif salary_from.isdigit():
            salary['from'] = int(salary_from)
            break
        elif not salary_from:
            salary['from'] = None
            break
        else:
            print("Сумма зарплаты должна быть в цифрах!")
    if request:
        while True:
            salary_to = input("Введите сумму зарплаты до, если не важно, нажмите ENTER,\n"
                              "для возврата к предыдущему меню введите EXIT:  ")
            if salary_to.lower() == 'exit':
                break
            elif salary_to.isdigit():
                salary['to'] = int(salary_to)
                break
            elif not salary_to:
                salary['to'] = None
                break
            else:
                print("Сумма зарплаты должна быть в цифрах!")
    return salary


def get_vacancies_by_salary(salary) -> None:
    """
    Получает вакансии из json-файла, фильтрует их по зарплате от и до и сохраняет обратно в файл
    :param salary: словарь с параметрами зарплаты от и до
    """
    if salary['from']:
        vac_obj_list = get_vacancies_from_file()
        vacancies_by_salary_from = Vacancy.get_vacancies_by_salary_from(vac_obj_list, salary['from'])
        Vacancy.save_to_file(vacancies_by_salary_from)
    if salary['to']:
        vac_obj_list = get_vacancies_from_file()
        vacancies_by_salary_to = Vacancy.get_vacancies_by_salary_to(vac_obj_list, salary['to'])
        Vacancy.save_to_file(vacancies_by_salary_to)


def printing_vacancies(vacancies: list) -> None:
    """
    Выводит информацию о каждой вакансии из полученного списка
    :param vacancies: список объектов класса Vacancy
    """
    for vacancy in vacancies:
        print(vacancy)
        # print(vacancy.resource)
        # print(vacancy.name)
        # print(vacancy.city)
        # print(vacancy.url)
        # print(vacancy.date_time)
        # print(f"{vacancy.salary_from} - {vacancy.salary_to} {vacancy.currency}")
        # print(vacancy.requirement)
    print(f"\nНайдено {len(vacancies)} вакансий\n#####################\n")