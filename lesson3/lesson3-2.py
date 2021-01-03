"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def print_user(**kwargs):
    form = {'name': None, 'surname': None, 'year_of_birth': None,
            'city': None, 'email': None, 'telephone': None}
    for key in kwargs.keys():
        form[key] = kwargs[key]
    list(map(lambda param: print(f'{param} - {form[param]}'), form.keys()))
    print('-'*30)


def run():
    tom_hardy = {'name': 'Tom', 'surname': 'Hardy', 'year_of_birth': 1977, 'city': 'London',
                 'email': 'tom_hardy@gmail.com', 'telephone': '+44207772377'}
    keanu_reeves = {'name': 'Keanu', 'surname': 'Reeves', 'year_of_birth': 1964}
    print_user(**tom_hardy)
    print_user(**keanu_reeves)


run()
