from utils import center_text, generating_spaces, reading_players

def dim_fun():
    texts = list()
    texts.append('=============== Загрузка сохраненной игры ===============')
    texts.append('                                                         ')
    texts.append('                    Выберите из списка                   ')
    texts.append('                    Выйти с модуля : q :                 ')
    texts.append('                                                         ')
    texts.append('=========================================================')
    center_text(texts) # центрирование и вывод текста

    while True:
        comand = input('Выберите сохранение: ')
        if comand not in map(str, range(3, 21)):
            whitespaces = generating_spaces() # Генерация пробелов
            print(f'{whitespaces}Такой команды не существует')
        else:
            global dim
            dim = int(comand)
            break
    return dim_fun