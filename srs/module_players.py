from utils import center_text, generating_spaces, reading_players
from sys import path
from pathlib import Path
from module_help import help_fun

selected_player = "0" # Выбранный игрок (можно изменить в меню)

def new_player_fun():
    """Функция создания игрока"""
    texts = list()
    texts.append('==================================================================')
    texts.append('                     Введите имя нового игрока:                   ')
    texts.append('==================================================================')
    center_text(texts) # центрирование и вывод текста
    
    whitespaces = generating_spaces() # Генерация пробелов
    
    # чтение списка игроков для избежания повторения
    Players = reading_players()
    Players.pop(-1)
    Players = list((pl.split(' '))[0].rstrip(':') for pl in Players)
    
    while True:
        new_name_player = input('Введите имя нового игрока:') # Ввод имени нового игрока
        
        # проверка на отсутствие игрока с анологичным именем "new_name_player"
        if new_name_player not in Players:
            print(f'{whitespaces}Создан игрок: {new_name_player};')
            data_file = Path(path[0]).parent / 'data/players.txt' # Поиск файла для сохранений в папке data
            new_statistics = {'побед': 0, 'поражений': 0, 'ничьих': 0} # статистика нового игрока
            # запись нового игрока в папке data файле players
            with open(data_file, 'a', encoding='utf-8') as filein:
                filein.write(f'{new_name_player}: {new_statistics}\n')
            from module_new_game import opening_a_new_game
            if opening_a_new_game == 'no':
                players_fun()
            break
        else:
            print(f'{whitespaces}Такой игрок уже существует')
        
    return new_player_fun
    
def choice_player_fun():
    """Функция выбора игрока"""
    from module_new_game import opening_a_new_game
    texts = list()
    texts.append('=====================================================================')
    texts.append('  Выберите нового игрока (введите в командную строку номер игрока):  ')
    texts.append('=====================================================================')
    center_text(texts) # центрирование и вывод текста
    
    # вывод списка игроков
    Players = reading_players()
    if Players[0] == '':
        Players = ""
    else:
        Players.pop(-1)
        Players = list((pl.split(' '))[0].rstrip(':') for pl in Players)
        whitespaces = generating_spaces() # Генерация пробелов
        for n in range(len(Players)):
            print(f'{whitespaces}{n + 1}. {Players[n]};')
            
    # Проверка на наличие игроков
    if Players == "":
        print(f'{whitespaces}Нету ни одного игрока')
        print(f'{whitespaces}Создайте игрока')
        new_player_fun()
    else:
        # Выбор игрока
        while True:
            comand = input('Выберите игрока: ')
            selects = list(str(n + 1) for n in range(len(Players)))
            # проверка на наличие игрока comand
            if comand not in selects:
                print(f'{whitespaces}Такого игрока не существует')
            else:
                global selected_player
                selected_player = comand
                print(f'{whitespaces}Выбран игрок: {Players[int(comand) - 1]};')
                from module_new_game import opening_a_new_game
                if opening_a_new_game == 'no':
                    players_fun()
                break
        
    return choice_player_fun

def players_fun():
    """Функция выбора игрока или его создания"""
    texts = list()
    texts.append('============РАЗДЕЛ СОЗДАНИЯ ИЛИ ПЕРЕКЛЮЧЕНИЯ НА ИГРОКА============')
    texts.append('                                                                  ')
    texts.append('                     создать нового игрока : np :                 ')
    texts.append('                            выбрать игрока : cp :                 ')
    texts.append('                              выйти : quit : q  : выход : в :     ')
    texts.append('                                                                  ')
    texts.append('==================================================================')
    
    center_text(texts) # центрирование и вывод текста
    
    # Шаблон для записи игроков
    Players = ""
    
    while True:
        comand = input('Введите команду: ')
        if comand == 'np':
            new_player_fun()
        if comand == 'cp':
            choice_player_fun()
        if comand == 'q' or comand == 'в':
            help_fun()
            break
        if comand not in ['np','cp','q']:
            whitespaces = generating_spaces() # Генерация пробелов
            print(f'{whitespaces}Такой команды не существует')
            
    return players_fun
            