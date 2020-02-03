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

if __name__ == "__main__":
    TEXT = 'привет, как дела!?'
    vocabluary = get_vocabluary(TEXT)
    print('\nСформированный словарь переводов слов из текста:')
    l_voc = list(vocabluary.items())
    l_voc.sort(key=lambda i: i[1])
    for key, value in l_voc:
        res = '| {0:<{1}} | {2:>{3}} |'.format(key, max_len(vocabluary.keys()), value, max_len(vocabluary.values()))
        print(res)
