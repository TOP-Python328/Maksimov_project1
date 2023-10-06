from random import choice
from math import ceil

def easy_bot(playing_field, stroke_boundary):
    while True:
        comand = choice(stroke_boundary)
        if playing_field[comand] == 0:
            break
    return comand
    
def hard_bot(playing_field, dim, stroke_boundary):
    moves = ''
    matrix_moves_bot = gen_matrix_moves_not_even_bot(playing_field, dim, stroke_boundary) # наилучший ход
    best_move = gen_parrying_pl_1(playing_field, dim, stroke_boundary) # парирование игрока
    finish_move = gen_finish(playing_field, dim, stroke_boundary) # финальный ход бота
    if finish_move != None:
        moves = finish_move
    elif best_move == None:
        moves = matrix_moves_bot
    else:
        moves = best_move
    return moves

# индексы для наименования ключей игровых клеток
abc_code = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']

def gen_finish(playing_field, dim, stroke_boundary):
    # функция финального хода бота
    matrix_moves_fin = dict()
    for N in range(dim):
        for n in range(dim):
            matrix_moves_fin[f'{abc_code[N]}{n + 1}'] = 0
    # присваивание 1 клетке с Токеном игрока №1
    for n in range(dim**2):
        if playing_field[stroke_boundary[n]] == 1:
            matrix_moves_fin[stroke_boundary[n]] = -1
    # присваивание -1 клетке с Токеном Бота
    for n in range(dim**2):
        if playing_field[stroke_boundary[n]] == 2:
            matrix_moves_fin[stroke_boundary[n]] = 1
    moves = list()
    moves_abc = list()
    for N in range(dim):
        motion = list()
        motion_abc = list()
        for n in range(dim):
            motion.append(matrix_moves_fin[f'{abc_code[N]}{n + 1}'])
            motion_abc.append(f'{abc_code[N]}{n + 1}')
        moves.append(sum(motion))
        moves_abc.append(motion_abc)
    for N in range(dim):
        motion = list()
        motion_abc = list()
        for n in range(dim):
            motion.append(matrix_moves_fin[f'{abc_code[n]}{N + 1}'])
            motion_abc.append(f'{abc_code[n]}{N + 1}')
        moves.append(sum(motion))
        moves_abc.append(motion_abc)
    motion = list()
    motion_abc = list()
    for N in range(dim):
        motion.append(matrix_moves_fin[f'{abc_code[N]}{N + 1}'])
        motion_abc.append(f'{abc_code[N]}{N + 1}')
    moves.append(sum(motion))
    moves_abc.append(motion_abc)
    motion = list()
    motion_abc = list()
    for N in range(dim):
        motion.append(matrix_moves_fin[f'{abc_code[dim - 1 - N]}{N + 1}'])
        motion_abc.append(f'{abc_code[dim - 1 - N]}{N + 1}')
    moves.append(sum(motion))
    moves_abc.append(motion_abc)
    best_move = list(i for i in range(len(moves)) if moves[i]==max(moves))
    best_move = choice(best_move)
    best_move = moves_abc[best_move]
    best_move = dict(list((k, v) for k, v in matrix_moves_fin.items() if k in best_move))
    max_val = sum(best_move.values())
    if max_val == (dim - 1):
        best_move = list(k for k, v in best_move.items() if v == min(best_move.values()))
        best_move = best_move[0]
    else:
        best_move = None
    return best_move

def gen_parrying_pl_1(playing_field, dim, stroke_boundary):
    # функция парирования игрока №1
    matrix_moves_bot = dict()
    for N in range(dim):
        for n in range(dim):
            matrix_moves_bot[f'{abc_code[N]}{n + 1}'] = 0
    # присваивание 1 клетке с Токеном игрока №1
    for n in range(dim**2):
        if playing_field[stroke_boundary[n]] == 1:
            matrix_moves_bot[stroke_boundary[n]] = 1
    # присваивание -1 клетке с Токеном Бота
    for n in range(dim**2):
        if playing_field[stroke_boundary[n]] == 2:
            matrix_moves_bot[stroke_boundary[n]] = -1
    moves = list()
    moves_abc = list()
    for N in range(dim):
        motion = list()
        motion_abc = list()
        for n in range(dim):
            motion.append(matrix_moves_bot[f'{abc_code[N]}{n + 1}'])
            motion_abc.append(f'{abc_code[N]}{n + 1}')
        moves.append(sum(motion))
        moves_abc.append(motion_abc)
    for N in range(dim):
        motion = list()
        motion_abc = list()
        for n in range(dim):
            motion.append(matrix_moves_bot[f'{abc_code[n]}{N + 1}'])
            motion_abc.append(f'{abc_code[n]}{N + 1}')
        moves.append(sum(motion))
        moves_abc.append(motion_abc)
    motion = list()
    motion_abc = list()
    for N in range(dim):
        motion.append(matrix_moves_bot[f'{abc_code[N]}{N + 1}'])
        motion_abc.append(f'{abc_code[N]}{N + 1}')
    moves.append(sum(motion))
    moves_abc.append(motion_abc)
    motion = list()
    motion_abc = list()
    for N in range(dim):
        motion.append(matrix_moves_bot[f'{abc_code[dim - 1 - N]}{N + 1}'])
        motion_abc.append(f'{abc_code[dim - 1 - N]}{N + 1}')
    moves.append(sum(motion))
    moves_abc.append(motion_abc)
    best_move = list(i for i in range(len(moves)) if moves[i]==max(moves))
    best_move = choice(best_move)
    best_move = moves_abc[best_move]
    best_move = dict(list((k, v) for k, v in matrix_moves_bot.items() if k in best_move))
    max_val = sum(best_move.values())
    if max_val == (dim - 1):
        best_move = list(k for k, v in best_move.items() if v == min(best_move.values()))
        best_move = best_move[0]
    else:
        best_move = None
    return best_move
    
def gen_matrix_moves_not_even_bot(playing_field, dim, stroke_boundary):
    # функция наилучшего хода бота
    matrix_moves_bot = dict()
    dim_count_R = (dim) # правая граница матрицы
    dim_count_L = 0 # левая граница матрицы
    for num in range(ceil(dim / 2)):
        for N in range(dim_count_L, dim_count_R):
            for n in range(dim_count_L, dim_count_R):
                matrix_moves_bot[f'{abc_code[N]}{n + 1}'] = num + 2
        dim_count_R -= 1
        dim_count_L += 1
    # присваивание нуля клетке с Токеном игрока №1
    for n in range(dim**2):
        if playing_field[stroke_boundary[n]] == 1:
            matrix_moves_bot[stroke_boundary[n]] = 0
    # присваивание наивысшей суммы клетке с Токеном Бота
    for n in range(dim**2):
        if playing_field[stroke_boundary[n]] == 2:
            matrix_moves_bot[stroke_boundary[n]] = 1
    # вычисление наилучшего хода для бота
    moves = list()
    moves_abc = list()
    for N in range(dim):
        motion = list()
        motion_abc = list()
        for n in range(dim):
            motion.append(matrix_moves_bot[f'{abc_code[N]}{n + 1}'])
            motion_abc.append(f'{abc_code[N]}{n + 1}')
        moves.append(sum(motion))
        moves_abc.append(motion_abc)
    for N in range(dim):
        motion = list()
        motion_abc = list()
        for n in range(dim):
            motion.append(matrix_moves_bot[f'{abc_code[n]}{N + 1}'])
            motion_abc.append(f'{abc_code[n]}{N + 1}')
        moves.append(sum(motion))
        moves_abc.append(motion_abc)
    for N in range(dim):
        motion = list()
        motion_abc = list()
        motion.append(matrix_moves_bot[f'{abc_code[N]}{N + 1}'])
        motion_abc.append(f'{abc_code[n]}{N + 1}')
        moves.append(sum(motion))
        moves_abc.append(motion_abc)
    for N in range(dim):
        motion = list()
        motion_abc = list()
        motion.append(matrix_moves_bot[f'{abc_code[dim - 1 - N]}{dim - N}'])
        motion_abc.append(f'{abc_code[n]}{N + 1}')
        moves.append(sum(motion))
        moves_abc.append(motion_abc)
    best_move = list(i for i in range(len(moves)) if moves[i]==max(moves))
    best_move = choice(best_move)
    best_move = moves_abc[best_move]
    best_move = dict(list((k, v) for k, v in matrix_moves_bot.items() if k in best_move))
    best_move = list(k for k, v in best_move.items() if v == max(best_move.values()))
    while True:
        best_move_fin = best_move[choice(range(len(best_move)))]
        if playing_field[best_move_fin] not in [1, 2]:
            break
    return best_move_fin