from utils import center_text, generating_spaces, reading_players
from module_help import help_fun
from module_players import players_fun
from module_new_game import run_start_game_fun
from module_new_game import new_game_fun
from module_dim import dim_fun
from module_save import save_load_fun
# Вспомогательный модуль

dim = 3 # размер игрового поля

help_fun() #---запуск начальной заставки "РАЗДЕЛ ПОМОЩИ"---

while True:
    comand = input('Введите команду: ') 
    if comand == 'n' or comand == 'н':
        run_start_game_fun()
    if comand == 'l' or comand == 'з':
        save_load_fun()
    if comand == 'h' or comand == 'п':
        help_fun()
    if comand == 'p' or comand == 'и':
        players_fun()
    if comand == 't' or comand == 'т':
        texts = list()
        texts.append('=============== Статистика игроков ===============')
        center_text(texts) # центрирование и вывод текста
        Players = reading_players()
        Players.pop(-1)
        whitespaces = generating_spaces() # Генерация пробелов
        for n in range(len(Players)):
            print(f'{whitespaces}{n + 1}. {Players[n]};')
    if comand == 'd' or comand == 'р':
        dim_fun()
    if comand == 'q' or comand == 'в':
        break
