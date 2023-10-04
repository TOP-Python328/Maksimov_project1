from utils import center_text

def help_fun() -> str:
    """Функция выводящая раздел помощи"""
    texts = list()
    texts.append('==========================РАЗДЕЛ ПОМОЩИ==========================')
    texts.append('                                                                 ')
    texts.append('                начать новую партию : new    : n : начать   : н :')
    texts.append('      загрузить существующую партию : load   : l : загрузка : з :')
    texts.append('           отобразить раздел помощи : help   : h : помощь   : п :')
    texts.append('создать или переключиться на игрока : player : p : игрок    : и :')
    texts.append('     отобразить таблицу результатов : table  : t : таблица  : т :')
    texts.append('               изменить размер поля : dim    : d : размер   : р :')
    texts.append('                              выйти : quit   : q : выход    : в :')
    texts.append('                                                                 ')
    texts.append('=================================================================')
    center_text(texts) # центрирование и вывод текста
    
    return help_fun
            