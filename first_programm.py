# task_input = (1, 1, 1)
#
# if task_input[0] > task_input[1] and task_input[0] > task_input[2]:
#     print('Максимальное число', task_input[0])
# elif task_input[1] > task_input[0] and task_input[1] > task_input[2]:
#     print('Максимальное число', task_input[1])
# else:
#     print('Максимальное число', task_input[2])

# x = 300
# # for i in range(2, x):
# #     if x % i == 0:
# #         print('Составное')
# #         break
# # else:
# #     print('Простое')

# input_matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 10]
# ]
# res = 0
# for i in range(len(input_matrix)):
#     res += input_matrix[i][i]
# print(res)

input_sentence = "the quik brown for jumps over the lazy dog"
res = [i for i in input_sentence.split(' ') if i != 'the']
print(res)