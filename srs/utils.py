from shutil import get_terminal_size
import os
from sys import path
from pathlib import Path

def center_text(texts):
    """Функция центрирования и вывода текста"""
    heigh_win = os.get_terminal_size().columns - 2; # ширина терминала (-2 на запас)
    max_heigh_text = len(max(texts)) # максимальная ширина текста
    # центрирование подсказок
    if max_heigh_text < heigh_win:
        for i in range(len(texts)):
            texts[i] = texts[i].center(heigh_win)
    # Граница модулей
    border = ""
    for n in range(heigh_win):
        border += "_"
    print(border)
    # преобразование в монолитный текст
    texts = '\n'.join(texts)
    return print(texts)
    
def generating_spaces():
    """Функция генерации пробелов"""
    heigh_win = os.get_terminal_size().columns - 2; # ширина терминала (-2 на запас)
    whitespaces = ""
    for n in range(int(heigh_win / 4)):
        whitespaces += " "
    return whitespaces
    
def reading_players():
    data_file = Path(path[0]).parent / 'data/players.txt' # Поиск файла для сохранений в папке data
    with open(data_file, 'r', encoding='utf-8') as filein:
        Players = filein.read()
        Players = Players.split('\n')
    return Players