# # l = ['a', 'b', 'c']
# # d = {'b': 'eee', 'a': 'uuu', 'd': 'xxx'}
# # i = 0
# # for i in range(len(l)):
# #     if l[i] in d.keys():
# #         l[i] = d[l[i]]
# # print(l)
# #
# # l = '$$ /// $$ $$$$ $$$$$$///////$'
# # lis = l.split('$')
# # ll = []
# # for i in range(len(lis)):
# #     if lis[i] != '':
# #         ll.append(lis[i])
# # print(ll)
# # print(lis)
# #
# # l = ['aaa', 'bbbbbbb', 'cc']
# # l1 = []
# # for i in l:
# #     l1.append(len(i))
# # print(max(l1))
#
# l = [['aa', 'bbb', 'c'], ['aaaaaa', 'b', 'cccccccccccccc'], ['asf', 'bnbnwenewnwenwe', 'c', 'sb']]
# l_res = []
# for i in range(len(l)):
#     l_res.append(len(l[i][2]))
# print(max(l_res))
# # print(max(l_res))

# def disemvowel(string):
#     l_str = []
#     for i in string:
#         if i.lower() not in 'aeiou':
#             l_str.append(i)
#     string = ''.join(l_str)
#     return string
#


def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

print(disemvowel('This website is for losers LOL!'))