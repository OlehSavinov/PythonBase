# # # # l = ['a', 'b', 'c']
# # # # # d = {'b': 'eee', 'a': 'uuu', 'd': 'xxx'}
# # # # # i = 0
# # # # # for i in range(len(l)):
# # # # #     if l[i] in d.keys():
# # # # #         l[i] = d[l[i]]
# # # # # print(l)
# # # # #
# # # # # l = '$$ /// $$ $$$$ $$$$$$///////$'
# # # # # lis = l.split('$')
# # # # # ll = []
# # # # # for i in range(len(lis)):
# # # # #     if lis[i] != '':
# # # # #         ll.append(lis[i])
# # # # # print(ll)
# # # # # print(lis)
# # # # #
# # # # # l = ['aaa', 'bbbbbbb', 'cc']
# # # # # l1 = []
# # # # # for i in l:
# # # # #     l1.append(len(i))
# # # # # print(max(l1))
# # # #
# # # # l = [['aa', 'bbb', 'c'], ['aaaaaa', 'b', 'cccccccccccccc'], ['asf', 'bnbnwenewnwenwe', 'c', 'sb']]
# # # # l_res = []
# # # # for i in range(len(l)):
# # # #     l_res.append(len(l[i][2]))
# # # # print(max(l_res))
# # # # # print(max(l_res))
# # #
# # # # def disemvowel(string):
# # # #     l_str = []
# # # #     for i in string:
# # # #         if i.lower() not in 'aeiou':
# # # #             l_str.append(i)
# # # #     string = ''.join(l_str)
# # # #     return string
# # # #
# # #
# # #
# # # # def disemvowel(s):
# # # #     for i in "aeiouAEIOU":
# # # #         s = s.replace(i,'')
# # # #     return s
# # # #
# # # # print(disemvowel('This website is for losers LOL!'))
# # #
# # # # def pillars(num_pill, dist, width):
# # # #     res = ((num_pill - 1) * dist * 100) + ((num_pill - 2) * width)
# # # #     if res < 0:
# # # #         res = 0
# # # #     return res
# # # #
# # # # def pillars(num_pill, dist, width):
# # # #     return dist * 100 * (num_pill - 1) + width * (num_pill - 2) * (num_pill > 1)
# # # #
# # # # print(pillars(1, 10, 10))
# # #
# # # # def double_char(s):
# # # # #     doud_s = ''.join([x * 2 for x in s])
# # # # #     return doud_s
# # # #
# # # # def double_char(s):
# # # #     res = ''
# # # #     for i in s:
# # # #         res += i*2
# # # #     return res
# # # #
# # # # print(double_char('1234!_ '))
# #
# # def solution(string):
# #     return string[::-1]
# #
# # print(solution('world'))
# #
# # def remove_char(s):
# #     return s[1:-1]
# #
# # print(remove_char('ok'))
# #
# # import math
# # # def litres(time):
# # #     return math.floor(time / 2)
# # #
# # # print(litres(0.82))
#
# def check_exam(arr1,arr2):
#     res = 0
#     for i in range(len(arr1)):
#         if arr1[i] == arr2[i]:
#             res += 4
#         elif arr2[i] != '':
#             res += -1
#     if res < 0:
#         res = 0
#     return res
#
# print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))
#
# def people_with_age_drink(age):
#     if age < 14:
#         d = 'drink toddy'
#     elif age < 18:
#         d = 'drink coke'
#     elif age < 21:
#         d = 'drink beer'
#     else:
#         d = 'drink whisky'
#     return d
#
# print(people_with_age_drink(22))
#
# def include(arr,item):
#     return item in arr
#
# print(include([1,2,5,4], 3))
#
# def vector_length(vector):
#     # return format(((((vector[1][0] - vector[0][0]) ** 2) + ((vector[1][1] - vector[0][1]) ** 2)) ** 0.5), '.7f')
#     return (((vector[1][0] - vector[0][0]) ** 2) + ((vector[1][1] - vector[0][1]) ** 2)) ** 0.5
# print(vector_length([[-3.9, -8.8],[-7.8, 1.7]]))

def sc(width,length,gaps):
    res = (width * 2 + (length - 2) * 2) / (gaps + 1)
    if res.is_integer():
        return int(res)
    return 0

print(sc(3,3,2))