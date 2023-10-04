from utils import center_text, generating_spaces, reading_players
from sys import path
from pathlib import Path
from module_players import new_player_fun, choice_player_fun
from module_play_game import play_game_players

selected_two_player = "0" # Выбранный второй игрок (можно изменить в меню)
opening_a_new_game = 'no' # запрет на возврат на run_start_game_fun
game_mode = ""
Token = ""

def single_player_fun():
    """Функция одиночной игры"""
    texts = list()
    texts.append('======================== ОДИНОЧНАЯ ИГРА =========================')
    texts.append('                                                                 ')
    texts.append('     ________________Выберите сложность игры:_______________     ')
    texts.append('                                                                 ')
    texts.append('                          Легкий  : e :                          ')
    texts.append('                          Сложный : h :                          ')
    texts.append('                                                                 ')
    texts.append('=================================================================')
    center_text(texts) # центрирование и вывод текста
    
    opening_a_new_game = 'no' # запрет на возврат на run_start_game_fun
    
    # цыкл выбора сложности игры
    while True:
        comand = input('выберите сложность игры: ')
        if comand == 'e':
            global game_mode
            game_mode = "easy"
            break
        if comand == 'h':
            global game_mode
            game_mode = "hard"
            break
        if comand not in ['e', 'h']:
            whitespaces = generating_spaces() # Генерация пробелов
            print(f'{whitespaces}Такой команды не существует')
            
    texts = list()
    texts.append('======================== ОДИНОЧНАЯ ИГРА =========================')
    texts.append('                                                                 ')
    texts.append('     _____________Выберите ТОКЕН для игрока №1:_____________     ')
    texts.append('                                                                 ')
    texts.append('                          Токен "X" : х :                        ')
    texts.append('                          Токен "O" : о :                        ')
    texts.append('                                                                 ')
    texts.append('=================================================================')
    center_text(texts) # центрирование и вывод текста
    
    # цыкл выбора токена в одиночной игре
    while True:
        comand = input('выберите токен для игрока №1: ')
        if comand == 'x':
            Token = "X"
            break
        if comand == 'o':
            Token = "O"
            break
        if comand not in ['x', 'o']:
            whitespaces = generating_spaces() # Генерация пробелов
            print(f'{whitespaces}Такой команды не существует')
    
    # запуск одиночной игры
    return play_game_players(1)
    
def game_of_two_fun():
    """Функция одиночной игры"""
    texts = list()
    texts.append('======================== ИГРА В ДВОЁМ =========================')
    texts.append('                                                               ')
    texts.append('     _________________Выберите игрока №2:________________      ')
    texts.append('                                                               ')
    texts.append('===============================================================')
    center_text(texts) # центрирование и вывод текста
    
    opening_a_new_game = 'no' # запрет на возврат на run_start_game_fun
    
    # проверка на наличие двух игроков (если нет двух игроков то игра выводит модуль создания доп игрока)
    Players = reading_players()
    if len(Players) < 3:
        new_player_fun()
    
    # вывод списка игроков
    whitespaces = generating_spaces() # Генерация пробелов
    Players = reading_players()
    Players.pop(-1)
    Players = list((pl.split(' '))[0].rstrip(':') for pl in Players)
    for n in range(len(Players)):
        print(f'{whitespaces}{n + 1}. {Players[n]};')
    
    # цыкл выбор второго игрока
    while True:
        comand = input('Выберите игрока: ')
        selects = list(str(n + 1) for n in range(len(Players)))
        from module_players import selected_player
        if comand not in selects:
            print(f'{whitespaces}Такого игрока не существует')
        elif comand == selected_player:
            print(f'{whitespaces}"Этот игрока выбрал игрок №1')
        else:
            global selected_two_player
            selected_two_player = comand
            print(f'{whitespaces}Выбран игрок: {Players[int(comand) - 1]};')
            break
    
    texts = list()
    texts.append('========================= ИГРА В ДВОЁМ ==========================')
    texts.append('                                                                 ')
    texts.append('     __________________Выберите свой ТОКЕН:_________________     ')
    texts.append('                                                                 ')
    texts.append('                          Токен "X" : х :                        ')
    texts.append('                          Токен "O" : о :                        ')
    texts.append('                                                                 ')
    texts.append('=================================================================')
    center_text(texts) # центрирование и вывод текста
    
    # цыкл выбора токена в игре вдвоем
    while True:
        comand = input('выберите свой токен: ')
        if comand == 'x':
            Token = "X"
            break
        if comand == 'o':
            Token = "O"
            break
        if comand not in ['e', 'h']:
            whitespaces = generating_spaces() # Генерация пробелов
            print(f'{whitespaces}Такой команды не существует')
    
    # запуск игры в двоем
    play_game_players(2)

    return game_of_two_fun

def new_game_fun():
    """Функция начала новой игры"""
    texts = list()
    texts.append('========================== НОВАЯ ИГРА ===========================')
    texts.append('                                                                 ')
    texts.append('     ___________________Выберите тип игры:__________________     ')
    texts.append('                                                                 ')
    texts.append('                      Одиночная игра : 1p :                      ')
    texts.append('                      Игра в двем    : 2p :                      ')
    texts.append('                                                                 ')
    texts.append('=================================================================')
    opening_a_new_game = 'no'
    
    center_text(texts) # центрирование и вывод текста
    
    # цыкл выбора режима игры
    while True:
        comand = input('Введите тип игры: ')
        if comand == '1p':
            single_player_fun()
            break
        if comand == '2p':
            game_of_two_fun()
            break
        if comand not in ['1p','2p']:
            whitespaces = generating_spaces() # Генерация пробелов
            print(f'{whitespaces}Такой команды не существует')
            
    return new_game_fun
        
def run_start_game_fun():
    """Функция запуска игры или вывода модуля создания нового игрока"""
    global opening_a_new_game
    opening_a_new_game = 'yes' # Разрешение на возврат на run_start_game_fun
    Players = ""
    data_file = Path(path[0]).parent / 'data/players.txt' # Поиск файла для сохранений в папке data
    with open(data_file, 'r', encoding='utf-8') as filein:
        Players = filein.read()
    # проверка на наличие игроков
    if Players == "":
        new_player_fun()
    from module_players import selected_player
    # проверка на наличие выбранного игрока
    if selected_player == '0':
        choice_player_fun()
    from module_players import selected_player
    # запуск функции новой игры
    if selected_player != '0': 
        new_game_fun()
    return run_start_game_fun