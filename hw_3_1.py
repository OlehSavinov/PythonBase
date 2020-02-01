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

for i in inp_text():

spl_text = inp_text().split()
d = dict()
for i in spl_text:
    d[i] = spl_text.count(i)
print(d)
