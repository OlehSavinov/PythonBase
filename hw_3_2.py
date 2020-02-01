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

t = inp_text().lower()
for i in punctuation:
    t = t.replace(i, ' ')
spl_text = t.split()
s = sorted(spl_text)

print('Введенные слова, отсортированные по алфавиту:')
for i in s:
    print(i)
