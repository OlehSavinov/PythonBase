from string import whitespace, punctuation

def max_len_keys(d):
    l = list(d.keys())
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

if __name__ == "__main__":
    TEXT = """Здесь определяется текст на котором будет продемонстрирована правильность работы программы.
    Текст должен быть многострочным.
    
    В тексте должны быть пустые строки
    и использоваться знаки из whitespace, например """ + "\t" + """табуляция"""
    vocabluary = get_vocabluary(TEXT)
    print('\nСформированный словарь переводов слов из текста:')
    for key, value in vocabluary.items():
        res = '{0:<{1}} --- {2}'.format(key, max_len_keys(vocabluary), value)
        print(res)
