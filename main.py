import datetime
import codecs
from tabulate import tabulate
from class_person import ClassPerson


def main():
    separator = '\n' + '-' * 30 + '\n'
    globals_ = globals()

    for i in range(1, 3):
        print(separator)
        globals_.get(f'task{i}')()


def task1():
    test = ClassPerson ('Поліщук', 'Карина',
                  datetime.datetime.strptime(str(input('Введіть дату [РР-ММ-ДД] -> ')), "%Y-%m-%d").date(),
                  'karina67')

    print(f"Вік контакту: {test.get_age()} років")
    print(f"Псевдонім контакту: {test.nickname}")
    print(test.get_fullname())


def task2():
    with codecs.open('files\\persons.txt', 'w', "utf-8") as fileText:
            table = [['Поліщук', 'Карина', '2004-05-18'],
                     ['Кисіль', 'Остап', '2004-07-05'],
                     ['Догма', 'Тимур', '2003-09-29']]
            fileText.writelines(tabulate(table, headers=["Surname", "Name", "Birth date"]))
            persons = ClassPerson.modifier('persons')

if __name__ == "__main__":
        main()