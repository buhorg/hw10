import json
import candidate

def get_data_from_json(filename):
    """
    Подключаем из json файла данные в виде списка словарей
    """
    with open(filename, encoding='utf-8') as file:
       candidates_data = json.load(file)
    return candidates_data


def get_candidates_list(filename, *args):
    """
    Получаем список с элементами - экземпляры класса Candidate.
    """
    candidates_data = get_data_from_json(filename)
    candidate_list = []
    for person in candidates_data:
        arguments = []
        for num in args:
            arguments.append(person[num])
        candidate_list.append(candidate.Candidate(arguments))
    return candidate_list


def get_person_by_id(my_id, candidate_list):
    """
    Проверка на удовлетворение экземпляра класса совпадению на id и распечатка
    """
    for person in candidate_list:
        if person.is_candidate_by_id(my_id):
            return person.print_candidate()
    return False


def get_person_by_skill(skill, candidate_list):
    """
    Проверка на удовлетворение экземпляра класса совпадению на skill и распечатка
    """
    my_str = ''
    for person in candidate_list:
        if person.is_candidate_by_skill(skill):
            my_str += person.print_candidate()
    return my_str


def print_candidate_list(candidate_list):
    """
    Распечатка в виде строки всего списка экземпляров класса Candidate
    """
    my_str = ''
    for person in candidate_list:
        my_str += person.print_candidate()
    return my_str


