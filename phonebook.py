FILE = 'data.txt'  # имя файла с данными


def show_all_contacts():

    ''' Постранично выводит записи на экран.
        lines - количество строк которые будут выводиться на экран
        file.read().splitlines() - делает построчный список из файла '''

    lines = 5
    with open(FILE, 'r') as file:
        nums = file.read().splitlines()
    sep = lines
    for num_line, line in enumerate(nums, start=1):
        print(num_line, line)
        if num_line == sep:
            input("\nНажмите 'Enter' для продолжения...\n")
            sep += lines


def add_contact():

    ''' Записывает новый контакт разделяя данные пробелом
    в Ф. И. О. делает первые буквы заглавными '''

    with open(FILE, 'a') as file:
        file.write(
            input("Введите фамилию: ").capitalize() + ' ' +
            input("Введите имя: ").capitalize() + ' ' +
            input("Введите отчество: ").capitalize() + ' ' +
            input("Введите организацию: ") + ' ' +
            input("Введите рабочий номер телефона: ") + ' ' +
            input("Введите личный номер телефона: ") + '\n')

        print('\nКонтакт успешно добавлен')


def edit_contact(query):

    ''' Обнавляет запись по личному номеру телефона 
    (предполагается что он уникальный)
    переделывает файл во вложеный список, перезаписывает
    нужную запись, переводит обратно в текст и записывает в файл'''

    with open(FILE, 'r') as file:
        nums = [line.split() for line in file]

    for i in range(len(nums)):
        if query in nums[i][5]:
            nums[i][0] = input("Введите фамилию: ").capitalize()
            nums[i][1] = input("Введите имя: ").capitalize()
            nums[i][2] = input("Введите отчество: ").capitalize()
            nums[i][3] = input("Введите организацию: ")
            nums[i][4] = input("Введите рабочий номер телефона: ")
            nums[i][5] = input("Введите личный номер телефона: ")

    string = ''
    for row in nums:
        for elem in row:
            string += elem + ' '
        string += '\n'

    with open(FILE, 'w') as file:
        file.write(string)
        print("\nКонтакт успешно отредактирован")


def find_contact(query):

    ''' Поиск контактов по одному из праметров: 
    фамилию, имя, отчество, организацию, рабочий номер телефона,
    личный номер телефона '''

    with open(FILE, 'r') as file:
        nums = [line.split() for line in file]

    for i in range(len(nums)):
        if query in nums[i]:
            print(nums[i][0], nums[i][1], nums[i][2], nums[i][3], nums[i][4],
                  nums[i][5])


def choice():

    ''' Меню для работы программы, где можно выбрать нужное действие '''

    selector = None
    try:
        selector = int(input("\nВведите '1' чтобы найти контакт\n" +
                             "Введите '2' чтобы добавить новый контакт\n" +
                             "Введите '3' чтобы редактировать контакт\n" +
                             "Введите '4' чтобы просмотреть все контакты\n" +
                             "Введите '5' чтобы выйти\n" +
                             "\nВвести здесь --->: "))
    except ValueError:
        print('\n\nНе корректный ввод!!!\n')
        print('Необходимо ввести целое число!!!\n\n')
    return selector


while True:
    selector = choice()

    if selector == 1:
        query = input('\nВведите слово или номер для поиска: ')
        find_contact(query)

    elif selector == 2:
        add_contact()

    elif selector == 3:
        query = input("\nВведите личный телефон контакта для редактирования: ")
        edit_contact(query)

    elif selector == 4:
        show_all_contacts()

    elif selector == 5:
        break
