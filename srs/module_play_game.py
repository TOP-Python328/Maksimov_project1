from utils import center_text, generating_spaces, reading_players
from sys import path
from pathlib import Path
from module_help import help_fun
from module_bot import easy_bot, hard_bot

# индексы для наименования ключей игровых клеток
abc_code = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']

def loading_playing_field(dim):
    # Функция генерации матрицы игрового поля
    playing_field = dict()
    for N in range(dim):
        for n in range(dim):
            playing_field[f'{abc_code[n]}{str(N + 1)}'] = 0
    return playing_field

def print_playing_field(dim, playing_field, Token, stroke_boundary):
    # Функция вывода игрового поля
    count = 0 # счет порядка матрицы поля
    for N in range(dim + 1):
        list_work = list()
        if N == 0:
            list_work = ['  ', ]
        else:
            if N <= 9:
                list_work = [f'{N}. ', ]
            else:
                list_work = [f'{N}.', ]
        for n in range(dim):
            if N == 0:
                list_work.append(f' {abc_code[n]} ')
            else:
                if playing_field[stroke_boundary[count]] == 0:
                    list_work.append('   ')
                if playing_field[stroke_boundary[count]] == 1:
                    if Token == 'X':
                        list_work.append(' X ')
                    else:
                        list_work.append(' O ')
                if playing_field[stroke_boundary[count]] == 2:
                    if Token == 'X':
                        list_work.append(' O ')
                    else:
                        list_work.append(' X ')
                count += 1
        if N == 0:
            list_work = ' '.join(list_work)
        else:
            list_work = ('|'.join(list_work)).replace('|', '', 1)
        print(list_work)
        if N != dim and N != 0:
            print('   ' + "".join(list('—' for n in range(len(list_work) - 2))))
    return print_playing_field
    
def gen_winning_combinations_fun(dim, stroke_boundary, playing_field, token_pl: int):
    # Функция генерации выигрышных комбинаций для игрока №1
    for N in range(dim):
        inning_combinations_pl_1 = list()
        for n in range(dim): 
            inning_combinations_pl_1.append(playing_field[stroke_boundary[(N*dim) + n]] == token_pl)
        if all(inning_combinations_pl_1) == True:
            winning_combinations = f'VICTORY'
            return winning_combinations
        inning_combinations_pl_1 = list()
        for n in range(dim): 
            inning_combinations_pl_1.append(playing_field[stroke_boundary[N + (n*dim)]] == token_pl)
        if all(inning_combinations_pl_1) == True:
            winning_combinations = f'VICTORY'
            return winning_combinations
    inning_combinations_pl_1 = list()
    for k in stroke_boundary[:dim**2:(dim + 1)]:
        inning_combinations_pl_1.append(playing_field[k] == token_pl)
    if all(inning_combinations_pl_1) == True:
        winning_combinations = f'VICTORY'
        return winning_combinations
    inning_combinations_pl_1 = list()
    for k in stroke_boundary[(dim-1):-1:(dim-1)]: 
        inning_combinations_pl_1.append(playing_field[k] == token_pl)
    if all(inning_combinations_pl_1) == True:
        winning_combinations = f'VICTORY'
        return winning_combinations
    winning_combinations = 'not VICTORY'
    return winning_combinations

def victory_player_1_fun(selected_player, selected_two_player):
    # Запись выигрыша игрока №1
    Players = reading_players()
    Players.pop(-1)
    New_Players = dict()
    for pl in Players:
        pl = pl.split(' ')
        pl = list(p.strip('{').strip(':').strip(',').strip("'").strip("'").strip("}") for p in pl)
        New_Players[pl[0]] = {pl[1]:int(pl[2]), pl[3]:int(pl[4]), pl[5]:int(pl[6])}
    New_Players[selected_player]['побед'] += 1
    New_Players[selected_two_player]['поражений'] += 1
    data_file = Path(path[0]).parent / 'data/players.txt' # Поиск файла для сохранений в папке data
    with open(data_file, 'w', encoding='utf-8') as filein:
        for k, v in New_Players.items():
            new_statistics = {'побед': v['побед'], 'поражений': v['поражений'], 'ничьих': v['ничьих']}
            filein.write(f'{k}: {new_statistics}\n')
    
    return victory_player_1_fun
    
def victory_player_2_fun(selected_player, selected_two_player):
    # Запись выигрыша игрока №2
    Players = reading_players()
    Players.pop(-1)
    New_Players = dict()
    for pl in Players:
        pl = pl.split(' ')
        pl = list(p.strip('{').strip(':').strip(',').strip("'").strip("'").strip("}") for p in pl)
        New_Players[pl[0]] = {pl[1]:int(pl[2]), pl[3]:int(pl[4]), pl[5]:int(pl[6])}
    New_Players[selected_player]['поражений'] += 1
    New_Players[selected_two_player]['побед'] += 1
    data_file = Path(path[0]).parent / 'data/players.txt' # Поиск файла для сохранений в папке data
    with open(data_file, 'w', encoding='utf-8') as filein:
        for k, v in New_Players.items():
            new_statistics = {'побед': v['побед'], 'поражений': v['поражений'], 'ничьих': v['ничьих']}
            filein.write(f'{k}: {new_statistics}\n')
    
    return victory_player_1_fun
 
def victory_bot_fun(selected_player):
    # Запись выигрыша Бота
    Players = reading_players()
    Players.pop(-1)
    New_Players = dict()
    for pl in Players:
        pl = pl.split(' ')
        pl = list(p.strip('{').strip(':').strip(',').strip("'").strip("'").strip("}") for p in pl)
        New_Players[pl[0]] = {pl[1]:int(pl[2]), pl[3]:int(pl[4]), pl[5]:int(pl[6])}
    New_Players[selected_player]['поражений'] += 1
    data_file = Path(path[0]).parent / 'data/players.txt' # Поиск файла для сохранений в папке data
    with open(data_file, 'w', encoding='utf-8') as filein:
        for k, v in New_Players.items():
            new_statistics = {'побед': v['побед'], 'поражений': v['поражений'], 'ничьих': v['ничьих']}
            filein.write(f'{k}: {new_statistics}\n')
    
    return victory_player_1_fun

def draw_fun(selected_player, selected_two_player):
    # Запись ничьи
    Players = reading_players()
    Players.pop(-1)
    New_Players = dict()
    for pl in Players:
        pl = pl.split(' ')
        pl = list(p.strip('{').strip(':').strip(',').strip("'").strip("'").strip("}") for p in pl)
        New_Players[pl[0]] = {pl[1]:int(pl[2]), pl[3]:int(pl[4]), pl[5]:int(pl[6])}
    New_Players[selected_player]['ничьих'] += 1
    New_Players[selected_two_player]['ничьих'] += 1
    data_file = Path(path[0]).parent / 'data/players.txt' # Поиск файла для сохранений в папке data
    with open(data_file, 'w', encoding='utf-8') as filein:
        for k, v in New_Players.items():
            new_statistics = {'побед': v['побед'], 'поражений': v['поражений'], 'ничьих': v['ничьих']}
            filein.write(f'{k}: {new_statistics}\n')
    
    return victory_player_1_fun

def save_fun(number_of_players, selected_player, selected_two_player, Token, game_mode, dim, save_moves):
    # Функция сохранения
    save_moves.reverse()
    if number_of_players == 1:
        selected_two_player = f'Бот_{game_mode}'
    save_file = [number_of_players, selected_player, selected_two_player, Token, game_mode, dim, save_moves]
    data_file = Path(path[0]).parent / 'data/save.txt' # Поиск файла для сохранений в папке data
    with open (data_file, 'a', encoding='utf-8') as filein:
        filein.write(f'{save_file}\n')
        print('Игра сохранена')
    return save_fun

def play_game_players(type_load: str, number_of_players: int):
    """Функция игры"""
    texts = list()
    if number_of_players == 1:
        texts.append(f'======================== ОДИНОЧНАЯ ИГРА =========================')
    else:
        texts.append(f'======================== ИГРА В ДВОЕМ =========================')
    texts.append(f'__________________(команда : s : - сохранение)__________________')
    center_text(texts) # центрирование и вывод текста
    
    save_text = list()
    count_save_text = 0
    
    if type_load == 'load':
        from module_save import save_text
        dim = save_text[5] # Размер игрового поля
        Token = save_text[3] # Токен игрока №1
        selected_player = save_text[1] # данные игрока №1
        selected_two_player = save_text[2] # данные игрока №2
        game_mode = save_text[4] # сложность игры
        count_save_text = len(save_text) - 6
    else:
        from module_dim import dim # Размер игрового поля
        from module_new_game import Token # Токен игрока №1
        from module_players import selected_player # данные игрока №1
        from module_new_game import selected_two_player # данные игрока №2
        from module_new_game import game_mode # сложность игры
        Players = reading_players()
        Players.pop(-1)
        Players = list((pl.split(' '))[0].rstrip(':') for pl in Players)
        selected_player = Players[int(selected_player) - 1]
        selected_two_player = Players[int(selected_two_player) - 1]
        
    playing_field = loading_playing_field(dim) # генерация матрицы игрового поля
    stroke_boundary = list(key for key in playing_field.keys()) # возможные ходы (ключи клеток)
    print_playing_field(dim, playing_field, Token, stroke_boundary) # вывод игрового поля
    
    whitespaces = generating_spaces() # Генерация пробелов
    save_moves = list()
    while True:
        if count_save_text !=0:
            comand = save_text[count_save_text + 5]
            count_save_text -= 1
            print(f'Ход игрока {selected_player}: ')
        else:
            comand = input(f'Ход игрока {selected_player}: ')
        # проверка на правильность ввода хода
        if comand == 's':
            save_fun(number_of_players, selected_player, selected_two_player, Token, game_mode, dim, save_moves)
        elif comand not in stroke_boundary:
            print(f'{whitespaces}Такой команды не существует')
        elif playing_field[comand] != 0:
            print(f'{whitespaces}На данную ячейку нельзя ходить')
        else:
            # ход игрока №1
            save_moves.append(comand)
            playing_field[comand] = 1
            print_playing_field(dim, playing_field, Token, stroke_boundary)
            winning_combinations = gen_winning_combinations_fun(dim, stroke_boundary, playing_field, 1)
            if winning_combinations != 'not VICTORY':
                victory_player_1_fun(selected_player, selected_two_player)
                print(f'{whitespaces}Победил игрок: {selected_player} !!!')
                break
            if all(list(v != 0 for k, v in playing_field.items())) == True:
                draw_fun(selected_player, selected_two_player)
                print(f'{whitespaces}НИЧЬЯ !!!')
                break
            if number_of_players == 1:
                while True:
                    # ход БОТА
                    if count_save_text !=0:
                        comand = save_text[count_save_text + 5]
                        count_save_text -= 1
                        print(f'Ход БОТА {game_mode}: ')
                    else:
                        print(f'Ход БОТА {game_mode}: ')
                        if game_mode == 'easy':
                            comand = easy_bot(playing_field, stroke_boundary)
                        else:
                            comand = hard_bot(playing_field, dim, stroke_boundary)
                    save_moves.append(comand)
                    playing_field[comand] = 2
                    break
            else:
                while True:
                    # ход игрока №2
                    if count_save_text !=0:
                        comand = save_text[count_save_text + 5]
                        count_save_text -= 1
                        print(f'Ход игрока {selected_two_player}: ')
                        break
                    else:
                        comand = input(f'Ход игрока {selected_two_player}: ')
                    if comand == 's':
                        save_fun(number_of_players, selected_player, selected_two_player, Token, game_mode, dim, save_moves)
                    elif comand not in stroke_boundary:
                        print(f'{whitespaces}Такой команды не существует')
                    elif playing_field[comand] != 0:
                        print(f'{whitespaces}На данную ячейку нельзя ходить')
                    else:
                        save_moves.append(comand)
                        playing_field[comand] = 2
                        break
            print_playing_field(dim, playing_field, Token, stroke_boundary)
            winning_combinations = gen_winning_combinations_fun(dim, stroke_boundary, playing_field, 2)
            if winning_combinations != 'not VICTORY':
                if number_of_players == 1:
                    victory_bot_fun(selected_player)
                    print(f'{whitespaces}Победил БОТ: {game_mode} !!!')
                else:
                    victory_player_2_fun(selected_player, selected_two_player)
                    print(f'{whitespaces}Победил игрок: {selected_two_player} !!!')
                break
            if all(list(v != 0 for k, v in playing_field.items())) == True:
                draw_fun(selected_player, selected_two_player)
                print(f'{whitespaces}НИЧЬЯ !!!')
                break
    
    return help_fun()