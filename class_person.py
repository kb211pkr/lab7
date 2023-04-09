from dateutil.relativedelta import relativedelta
import datetime
import codecs
from tabulate import tabulate

class ClassPerson:
    """
      Клас Person, який відображає запис в книзі контактів.
      Клас має 4 атрибута:
      - surname - рядок - прізвище контакту (обов'язковий)
      - first_name - рядок - ім'я контакту (обов'язковий)
      - nickname - рядок - псевдонім (опціональний)
      - birth_date - об'єкт datetime.date (обов'язковий)
      """

    def __init__(self, surname, first_name, birth_date, nickname=''):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        self.birth_date = birth_date

    def get_age(self):
       return (datetime.datetime.now() - relativedelta(years=self.birth_date.year)).year

    def get_fullname(self):
        return self.surname + ' ' + self.first_name

    @staticmethod
    def modifier(filename):
        persons = []
        with codecs.open(f'files\\{filename}.txt', 'r', "utf-8") as fileRead:
            with codecs.open(f'files\\{filename}Modifier.txt', 'w', "utf-8") as fileWrite:
                table = []
                count = 0
                for i in fileRead.readlines():
                    if count > 1:
                        line = i.split()
                        persons.append(
                            ClassPerson(line[0], line[1], datetime.datetime.strptime(line[2], "%Y-%m-%d").date()))
                        table.append([line[0], line[1], persons[count - 2].get_fullname(), line[2],
                                      persons[count - 2].get_age()])
                    count += 1
                headers = ['Surname', 'Name', 'Fullname', 'Birth date', 'Age']
                fileWrite.writelines(tabulate(table, headers=headers))
        return persons