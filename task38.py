def ask_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = int(input('Введите номер телефона: '))
    return last_name, first_name, phone_number


def save_to_file(data: tuple, file, mode='a'):
    data_str = ' '.join(map(str, data))
    # print(data_str)
    # 'cp-1251'
    with open(file, mode, encoding='utf-8') as fd:
        fd.write(f'{data_str}\n')

def read_file(file):
    with open(file, 'a', encoding='utf-8') as fd:
        lines = fd.readlines()
    headers = ['фамилия', 'имя', 'номер телефона']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
    return list_contacts

def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'фамилия', '2': 'имя', '3': 'номер телефона'}

def ask_search():
    print('По какому полю выполнить поиск?')
    search_param = input('1 - по фамилии, 2 - по имени, 3 - по номеру телефона: ')
    what = None
    if search_param == '1':
        what = input('Введите фамилию для поиска: ')
    elif search_param == '2':
        what = input('Введите имя для поиска: ')
    elif search_param == '3':
        what = input('Введите номер для поиска: ')
    return search_param, what




if __name__ == '__main__':
    file_contacts = 'file.txt'
    # data = ask_user()
    # print(data)
    # save_to_file(data, file_contacts)
    lst_contacts = read_file(file_contacts)
    print(lst_contacts)
    search_param, what = ask_search()
    search_contact(lst_contacts, search_param, what)
    # lst1 = [1, 2, 3]
    # lst2 = [7, 8, 9]
    # res = zip(lst1, lst2)
    # print(dict(res))

