from src.hh import HeadHunter
from src.superjob import SuperJob
from src.vacancy import Vacancy


def get_vacancies_by_api() -> None:
    keyword = input("Введите название профессии или слово для поиска вакансии.\n"
                    "Если хотите вызвать весь список, то нажмите ENTER: ")
    print("Просьба ожидать, идет формирование списка вакансий")
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
    salary = {'from': None, 'to': None}
    request = True
    while True:
        salary_from = input("Введите сумму зарплаты 'от', или нажмите ENTER,\n"
                            "Для возврата к меню введите EXIT:  ")
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
            salary_to = input("Введите сумму зарплаты 'до', если не важно, нажмите ENTER,\n"
                              "Для возврата к меню введите EXIT:  ")
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
    if salary['from']:
        vac_obj_list = get_vacancies_from_file()
        vacancies_by_salary_from = Vacancy.get_vacancies_by_salary_from(vac_obj_list, salary['from'])
        Vacancy.save_to_file(vacancies_by_salary_from)
    if salary['to']:
        vac_obj_list = get_vacancies_from_file()
        vacancies_by_salary_to = Vacancy.get_vacancies_by_salary_to(vac_obj_list, salary['to'])
        Vacancy.save_to_file(vacancies_by_salary_to)


def printing_vacancies(vacancies: list) -> None:
    for vacancy in vacancies:
        print(vacancy)
    print(f"\nНайдено {len(vacancies)} вакансий")
