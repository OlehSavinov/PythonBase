# # # # # # # # # l = ['a', 'b', 'c']
# # # # # # # # # # d = {'b': 'eee', 'a': 'uuu', 'd': 'xxx'}
# # # # # # # # # # i = 0
# # # # # # # # # # for i in range(len(l)):
# # # # # # # # # #     if l[i] in d.keys():
# # # # # # # # # #         l[i] = d[l[i]]
# # # # # # # # # # print(l)
# # # # # # # # # #
# # # # # # # # # # l = '$$ /// $$ $$$$ $$$$$$///////$'
# # # # # # # # # # lis = l.split('$')
# # # # # # # # # # ll = []
# # # # # # # # # # for i in range(len(lis)):
# # # # # # # # # #     if lis[i] != '':
# # # # # # # # # #         ll.append(lis[i])
# # # # # # # # # # print(ll)
# # # # # # # # # # print(lis)
# # # # # # # # # #
# # # # # # # # # # l = ['aaa', 'bbbbbbb', 'cc']
# # # # # # # # # # l1 = []
# # # # # # # # # # for i in l:
# # # # # # # # # #     l1.append(len(i))
# # # # # # # # # # print(max(l1))
# # # # # # # # #
# # # # # # # # # l = [['aa', 'bbb', 'c'], ['aaaaaa', 'b', 'cccccccccccccc'], ['asf', 'bnbnwenewnwenwe', 'c', 'sb']]
# # # # # # # # # l_res = []
# # # # # # # # # for i in range(len(l)):
# # # # # # # # #     l_res.append(len(l[i][2]))
# # # # # # # # # print(max(l_res))
# # # # # # # # # # print(max(l_res))
# # # # # # # #
# # # # # # # # # def disemvowel(string):
# # # # # # # # #     l_str = []
# # # # # # # # #     for i in string:
# # # # # # # # #         if i.lower() not in 'aeiou':
# # # # # # # # #             l_str.append(i)
# # # # # # # # #     string = ''.join(l_str)
# # # # # # # # #     return string
# # # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # # def disemvowel(s):
# # # # # # # # #     for i in "aeiouAEIOU":
# # # # # # # # #         s = s.replace(i,'')
# # # # # # # # #     return s
# # # # # # # # #
# # # # # # # # # print(disemvowel('This website is for losers LOL!'))
# # # # # # # #
# # # # # # # # # def pillars(num_pill, dist, width):
# # # # # # # # #     res = ((num_pill - 1) * dist * 100) + ((num_pill - 2) * width)
# # # # # # # # #     if res < 0:
# # # # # # # # #         res = 0
# # # # # # # # #     return res
# # # # # # # # #
# # # # # # # # # def pillars(num_pill, dist, width):
# # # # # # # # #     return dist * 100 * (num_pill - 1) + width * (num_pill - 2) * (num_pill > 1)
# # # # # # # # #
# # # # # # # # # print(pillars(1, 10, 10))
# # # # # # # #
# # # # # # # # # def double_char(s):
# # # # # # # # # #     doud_s = ''.join([x * 2 for x in s])
# # # # # # # # # #     return doud_s
# # # # # # # # #
# # # # # # # # # def double_char(s):
# # # # # # # # #     res = ''
# # # # # # # # #     for i in s:
# # # # # # # # #         res += i*2
# # # # # # # # #     return res
# # # # # # # # #
# # # # # # # # # print(double_char('1234!_ '))
# # # # # # #
# # # # # # # def solution(string):
# # # # # # #     return string[::-1]
# # # # # # #
# # # # # # # print(solution('world'))
# # # # # # #
# # # # # # # def remove_char(s):
# # # # # # #     return s[1:-1]
# # # # # # #
# # # # # # # print(remove_char('ok'))
# # # # # # #
# # # # # # # import math
# # # # # # # # def litres(time):
# # # # # # # #     return math.floor(time / 2)
# # # # # # # #
# # # # # # # # print(litres(0.82))
# # # # # #
# # # # # # def check_exam(arr1,arr2):
# # # # # #     res = 0
# # # # # #     for i in range(len(arr1)):
# # # # # #         if arr1[i] == arr2[i]:
# # # # # #             res += 4
# # # # # #         elif arr2[i] != '':
# # # # # #             res += -1
# # # # # #     if res < 0:
# # # # # #         res = 0
# # # # # #     return res
# # # # # #
# # # # # # print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))
# # # # # #
# # # # # # def people_with_age_drink(age):
# # # # # #     if age < 14:
# # # # # #         d = 'drink toddy'
# # # # # #     elif age < 18:
# # # # # #         d = 'drink coke'
# # # # # #     elif age < 21:
# # # # # #         d = 'drink beer'
# # # # # #     else:
# # # # # #         d = 'drink whisky'
# # # # # #     return d
# # # # # #
# # # # # # print(people_with_age_drink(22))
# # # # # #
# # # # # # def include(arr,item):
# # # # # #     return item in arr
# # # # # #
# # # # # # print(include([1,2,5,4], 3))
# # # # # #
# # # # # # def vector_length(vector):
# # # # # #     # return format(((((vector[1][0] - vector[0][0]) ** 2) + ((vector[1][1] - vector[0][1]) ** 2)) ** 0.5), '.7f')
# # # # # #     return (((vector[1][0] - vector[0][0]) ** 2) + ((vector[1][1] - vector[0][1]) ** 2)) ** 0.5
# # # # # # print(vector_length([[-3.9, -8.8],[-7.8, 1.7]]))
# # # # # #
# # # # # # def sc(width,length,gaps):
# # # # # #     res = (width * 2 + (length - 2) * 2) / (gaps + 1)
# # # # # #     if res.is_integer():
# # # # # #         return int(res)
# # # # # #     return 0
# # # # # #
# # # # # # print(sc(3,3,2))
# # # # # #
# # # # # # def make_2d_list(head,row,col):
# # # # # #     res, r = [], []
# # # # # #     for i in range(row):
# # # # # #         for j in range(col):
# # # # # #             res.append(j + head + i * col)
# # # # # #         r.append(res)
# # # # # #         res = []
# # # # # #     return r
# # # # # # print(make_2d_list(10**10,2,2))
# # # # # #
# # # # # # def largest_sum(s):
# # # # # #     l = [list(i) for i in s.split('0')]
# # # # # #     for i in range(len(l)):
# # # # # #         for j in range(len(l[i])):
# # # # # #             l[i][j] = int(l[i][j])
# # # # # #     res = [sum(l[i]) for i in range(len(l))]
# # # # # #     return max(res)
# # # # # #
# # # # # # print(largest_sum('0'))
# # # # #
# # # # # def unused_digits(*args):
# # # # #     s = set(''.join(map(str, args)))
# # # # #     res = ''
# # # # #     for i in '0123456789':
# # # # #         if i not in s:
# # # # #             res += i
# # # # #     return res
# # # # #
# # # # # print(unused_digits(643))
# # # #
# # # # def getCount(inputStr):
# # # #     num_vowels = 0
# # # #     for i in inputStr:
# # # #         if i in 'aeiou':
# # # #             num_vowels += 1
# # # #     return num_vowels
# # # #
# # # # print(getCount('abracadabra'))
# # #
# # # def to_1D(x, y, size):
# # #     return size[0] * y + x
# # #
# # # def to_2D(n, size):
# # #     x = n % size[0]
# # #     y = n // size[0]
# # #     return x, y
# # #
# # # print(to_2D(7, (1,8)))
# # def paint_letterboxes(start, finish):
# #     s = ''.join([str(i) for i in list(range(start, finish + 1))])
# #     res = [s.count(i) for i in '0123456789']
# #     return res
# #
# # print(paint_letterboxes(125, 132))
# def mystery():
#     results = {
#     'sanity': 'Hello'}
#     return results
#
# print(mystery())

# def reverse_fun(n):
#     res = []
#     for i in range(len(n)):
#         m = n[::-1]
#         res.append(m[i])
#         res.append(n[i])
#     return ''.join(res[:len(res) // 2])
#
# print(reverse_fun('012345'))

# def reverse_fun(n):
#     for i in range(len(n)):
#         n = n[:i] + n[i:][::-1]
#     return n
#
# print(reverse_fun('012345'))
#
# n = list('012345')
# print(n[1:][::-1])

# def get_free_urinals(urinals):
#     urinals = list(urinals)
#     res = 0
#     if len(urinals) == 1:
#         if urinals[0] == '0':
#             return 1
#         if urinals[0] == '1':
#             return 0
#     else:
#         for j in range(len(urinals)-1):
#             if urinals[j] == '1' and urinals[j+1] == '1':
#                 return -1
#         if urinals[0] == '0' and urinals[1] != '1':
#             res = 1
#             urinals[0] = '1'
#         if urinals[-1] == '0':
#             if urinals[-2] == '0':
#                 res += 1
#             urinals[-1] = '1'
#         for i in range(len(urinals)):
#             if urinals[i] == '0' and urinals[i+1] != '1' and urinals[i-1] != '1':
#                 res += 1
#                 urinals[i] = '1'
#         return res
#
# print(get_free_urinals('1'))
#
# def get_free_urinals(urinals):
#     return -1 if '11' in urinals else sum(((len(l)-1)//2 for l in f'0{urinals}0'.split('1')))
#
# print(get_free_urinals('1'))
#
# def high_and_low(numbers):
#     a = list(map(int, numbers.split(' ')))
#     return str(max(a)) + ' ' + str(min(a))
#
# print(high_and_low('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'))
#
# def name_file(fmt, nbr, start):
#     if isinstance(nbr, int) and isinstance(start, int):
#         a = [fmt for i in range(nbr)]
#         for i in range(len(a)):
#             a[i] = a[i].replace('<index_no>', str(start))
#             start += 1
#         return a
#     else:
#         return []
#
# print(name_file('file <index_no>', 0.2, 0))
# def solve(s):
#     o = [i for i in s if not i.isalnum()]
#     res = [sum(map(str.isupper, s)), sum(map(str.islower, s)), sum(map(str.isnumeric, s)), len(o)]
#     return res
#
# print(solve('Codewars@codewars123.com'))

#
# def celsius_to_romer(temp):
#     return temp * 0.525 + 7.5
#
# print(celsius_to_romer(24))
# import math
# def center(strng, width, fill=' '):
#     if width == 0:
#         return strng
#     elif strng == '':
#         return fill * width
#     else:
#         return math.ceil((width - len(strng)) / 2) * fill + strng + (width - len(strng)) // 2 * fill
#
# print(center('a', 2, '_'))
#
# def VampireNumber(k):
#     # rr = [x * y for x in range(11, 850) for y in range(x, int('9' * int(len(str(x))))) if sorted(list(str(x * y))) == sorted(str(x) + str(y))]
#     # rr.sort()
#     res = []
#     for x in range(11, 850):
#         for y in range(x, int('9' * int(len(str(x))))):
#             if str(x)[-1] != 0 or str(y)[-1] != 0:
#                 m = str(x * y)
#                 n = str(x) + str(y)
#                 if sorted(list(m)) == sorted(n):
#                     res.append(int(m))
#     res.sort()
#     r = res[k-1]
#     return r
#
#
# print(VampireNumber(150))

# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#     def is_worth_it(self):
#         return True if self.draft - (self.crew * 1.5) > 20 else False
#
# EmptyShip = Ship(1, 1)
# print(Ship.is_worth_it(EmptyShip))
# def remove(s):
#     n = 0
#     for i in s[::-1]:
#         if i == '!':
#             n += 1
#         else:
#             return s.replace('!', '') + '!' * n
#
# print(remove('Hi!!!!!! Hi!!!!!'))
#
# def accum(s):
#     return '-'.join(list(map(str.capitalize, [s[i] * (i + 1) for i in range(len(s))])))
#
# print(accum("NyffsGeyylB"))

def no_musical(start_class, end_class, musical_performed_every, enrolment_duration):
    if musical_performed_every == 0:
        return end_class - start_class + 1
    else:
        res = 0
        n = list(range(start_class, end_class + 1 + enrolment_duration))
        for i in range(len(n)):
            if i % musical_performed_every == 0:
                n[i] = 0
        m = [(n[i:enrolment_duration+i]) for i in range(len(n) - enrolment_duration)]
        for i in m:
            if 0 not in i:
                res += 1
        return res


print(no_musical(2603, 2765, 8, 4))

# if musical_performed_every == 0:
#     return end_class - start_class + 1
# else:
# #      n = [start_class + i for i in range(0, end_class - start_class + 1, musical_performed_every)]
# # #     # m = [(start_class + i, start_class + i + enrolment_duration) for i in range(0, end_class - start_class + 1)]
# # #     res = end_class - start_class - (len(n) - 1) * enrolment_duration
# # #     if res > 0:
# # #         return res
# # #     else:
# # #         return 0
# #      t = end_class - start_class + 1
# #      res = ((len(n) - 1) * enrolment_duration + 1)
# #      if res > 0:
# #         return res
# #      else:
# #         return 0
