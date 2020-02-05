l = ['a', 'b', 'c']
d = {'b': 'eee', 'a': 'uuu', 'd': 'xxx'}
i = 0
for i in range(len(l)):
    if l[i] in d.keys():
        l[i] = d[l[i]]
print(l)

l = '$$ /// $$ $$$$ $$$$$$///////$'
lis = l.split('$')
# for i in range(len(lis)):
#     if lis[i] == '':
#             print('f')

li = [1, 2]
print(len(li))
print(range(2))
