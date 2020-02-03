from string import punctuation

def inp_text():
    s = str()
    while True:
        text = input('Введите текст: ')
        if not text:
            break
        else:
            s += text + ' '
    return s

def max_len(d):
    l = list(d)
    m = l[0]
    for i in l[1:]:
        if len(i) > len(m):
            m = i
    return len(m)

t = inp_text().lower()
for i in punctuation:
    t = t.replace(i, ' ')
spl_text = t.split()
d = dict()
for i in spl_text:
    d[i] = str(spl_text.count(i))

print('Статистика слов:')
for key, value in d.items():
    res = '| {0:<{1}} | {2:>{3}} |'.format(key, max_len(d.keys()), value, max_len(d.values()))
    print(res)
