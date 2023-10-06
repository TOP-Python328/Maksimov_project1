from utils import center_text, generating_spaces, reading_players
from module_help import help_fun

dim = 3 # размер игрового поля

def dim_fun():
    texts = list()
    texts.append('=============== Установка размера игрового поля ===============')
    texts.append('                                                               ')
    texts.append('                Установите размер игрового поля                ')
    texts.append('                (от 3 до 20 клеток)                            ')
    texts.append('                                                               ')
    texts.append('===============================================================')
    center_text(texts) # центрирование и вывод текста

    while True:
        comand = input('Введите размер игрового поля: ')
        if comand not in map(str, range(3, 21)):
            whitespaces = generating_spaces() # Генерация пробелов
            print(f'{whitespaces}Такой команды не существует')
        else:
            global dim
            dim = int(comand)
            help_fun()
            break
    return dim_fun