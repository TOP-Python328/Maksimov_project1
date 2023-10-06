from utils import center_text, generating_spaces, reading_players
from sys import path
from pathlib import Path
from module_play_game import play_game_players
from module_help import help_fun

save_text = list()

def save_load_fun():
    texts = list()
    texts.append('=============== Загрузка сохраненной игры ===============')
    texts.append('                                                         ')
    texts.append('            Выберите сохрарение из списка                ')
    texts.append('                  (Выйти с модуля : q :)                 ')
    texts.append('                                                         ')
    texts.append('=========================================================')
    center_text(texts) # центрирование и вывод текста
    
    whitespaces = generating_spaces() # Генерация пробелов
    
    data_file = Path(path[0]).parent / 'data/save.txt' # Поиск файла для сохранений в папке data
    global save_text
    with open(data_file, 'r', encoding='utf-8') as filein:
        save_text = filein.read()
        save_text = save_text.split('\n')
        save_text.pop(-1)
        for n in range(len(save_text)):
            print(f'{whitespaces}{n+1}. {save_text[n]}')
    while True:
        comand = input('Выберите сохранение: ')
        if comand == 'q':
            help_fun()
            break
        elif comand not in list(map(str, range(1, (len(save_text) + 1)))):
            print(f'{whitespaces}Такого сохранения не существует')
        else:
            save_text = save_text[int(comand) - 1]
            save_text = save_text.split(' ')
            save_text = list(st.strip('[').strip(']]').strip(',').strip("'").rstrip("'") for st in save_text)
            save_text[0] = int(save_text[0])
            save_text[5] = int(save_text[5])
            play_game_players('load', save_text[0])
            break
    return save_load_fun