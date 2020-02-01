from string import whitespace, punctuation

def inp_text():
    s = str()
    while True:
        text = input('Введите текст: ')
        if not text:
            break
        else:
            s += text + ' '
    return s

# print(inp_text())

t = inp_text()
for i in punctuation:
    t = t.replace(i, ' ')

spl_text = t.split()
d = dict()
for i in spl_text:
    d[i] = spl_text.count(i)
print(d)
