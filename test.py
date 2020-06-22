import sys

# class Node:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.state = None

# def main():
#     x, y = map(int, input().split())
#     start = []
#     goal =[]
#     maze_node = [[Node(i, j) for j in range(y)] for i in range(x)]
#     for i in range(x):
#         maze_state = input()
#         for j in range(y):
#             maze_node[i][j].state = maze_state[j]
#             if maze_state[j] == 'S':
#                 start.append(maze_node[i][j].x)
#                 start.append(maze_node[i][j].y)
#             if maze_state[j] == 'G':
#                 goal.append(maze_node[i][j].x)
#                 goal.append(maze_node[i][j].y)


#     #移動すべきマス
#     go_x = int(goal[0]) - int(start[0])
#     go_y = int(goal[1]) - int(start[1])
#     go_sum = go_x + go_y
#     result = 100

#     for i in range(2**go_sum):
#         i_bin = bin(i)
#         new_i_bin = i_bin[2:]
#         sum_i_bin = 0
#         for j in range(len(new_i_bin)):
#             sum_i_bin += int(new_i_bin[j])
#         if sum_i_bin == go_x:
#             const = 0
#             for s in range(len(new_i_bin)):
#                 if new_i_bin[s] == '0':
#                     start[0] += 1
#                     const += 1
#                 else:
#                     start[1] += 1
#                     const += 1
#             if const < result:
#                 result = const
#     print(const)

# import sys

# def main():
#     d, r = map(int, input().split())
#     m = int(input())
#     n = list(map(int, input().split()))

#     if n[0] == 1:
#         print('0')
#     else:
#         enemy_list = list(range(d, r + 1))
#         for i in range(m):
#             const = n[i]
#             const_min = int(d/const)
#             const_max = int(r/const)
#             for j in range(const_min, const_max + 1):
#                 target = const * j
#                 if target in enemy_list:
#                     enemy_list.remove(target)
#         print(len(enemy_list))

# if __name__ == '__main__':
#     main()

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def main():
    x = make_divisors(60)
    print(x)


if __name__ == '__main__':
    main()
