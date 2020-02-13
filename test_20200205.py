# l = ['a', 'b', 'c']
# d = {'b': 'eee', 'a': 'uuu', 'd': 'xxx'}
# i = 0
# for i in range(len(l)):
#     if l[i] in d.keys():
#         l[i] = d[l[i]]
# print(l)
#
# l = '$$ /// $$ $$$$ $$$$$$///////$'
# lis = l.split('$')
# ll = []
# for i in range(len(lis)):
#     if lis[i] != '':
#         ll.append(lis[i])
# print(ll)
# print(lis)

l = ['aaa', 'bbbbbbb', 'cc']
l1 = []
for i in l:
    l1.append(len(i))
print(max(l1))
