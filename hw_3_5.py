from string import whitespace, punctuation

def max_len(d):
    l = list(d)
    m = l[0]
    for i in l[1:]:
        if len(i) > len(m):
            m = i
    return len(m)

def input_translate(i):
    while True:
        t = input('Введите перевод слова "{0}": '.format(i))
        swp = set(whitespace + punctuation)
        t_set = set(t)
        if t_set.issubset(swp):
            continue
        else:
            return t

def get_vocabluary(text):
    result = {}
    t = text.lower()
    for i in punctuation:
        t = t.replace(i, ' ')
    spl_text = set(t.split())
    for i in spl_text:
        result[i] = input_translate(i)
    return result

def t_whitespace(t):
    for i in t:
        if i not in (whitespace + punctuation):
            t = t.lower().replace(i, '$')
    t = t.split('$')
    t_w = []
    for i in range(len(t)):
        if t[i] != '':
            t_w.append(t[i])
    return t_w

def translate(text, dictionary):
    for i in punctuation:
        text = text.lower().replace(i, ' ')
    spl_text = text.split()
    for i in range(len(spl_text)):
        if spl_text[i] in vocabluary.keys():
            spl_text[i] = vocabluary[spl_text[i]]
    res_list = []
    if text[0] in whitespace and text[-1] in whitespace:
        for i in range(len(spl_text)):
            res_list.append(spl_text[i])
            res_list.append(t_whitespace(TEXT)[i+1])
    elif text[0] in whitespace:
        for i in range(len(spl_text)):
            res_list.append(t_whitespace(TEXT)[i])
            res_list.append(spl_text[i])
        del res_list[0]
    elif text[-1] not in whitespace:
        res_list.append(spl_text[0])
        for i in range(len(spl_text)-1):
            res_list.append(t_whitespace(TEXT)[i])
            res_list.append(spl_text[i+1])
    else:
        for i in range(len(spl_text)):
            res_list.append(spl_text[i])
            res_list.append(t_whitespace(TEXT)[i])
    res = ''.join(res_list)
    return res


if __name__ == "__main__":
    TEXT = """.Здесь определяется текст на котором будет продемонстрирована правильность работы программы.
    Текст должен быть многострочным.
    
    В тексте должны быть пустые строки
    и использоваться знаки из whitespace, например """ + "\t" + """табуляция"""
    vocabluary = get_vocabluary(TEXT)
    print('\nСформированный словарь переводов слов из текста (перевод упорядочен по алфавиту):')
    l_voc = list(vocabluary.items())
    l_voc.sort(key=lambda i: i[1])
    for key, value in l_voc:
        res = '| {0:<{1}} | {2:>{3}} |'.format(key, max_len(vocabluary.keys()), value, max_len(vocabluary.values()))
        print(res)
    print('\nПереведенный текст:')
    print(translate(TEXT, vocabluary))
