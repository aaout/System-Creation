import random

import matplotlib.pyplot as plt
import numpy as np


#ノードの状態を確保するクラスを作成
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wall = True
        self.g = 0

        #Q値の初期化
        #左から順に停止、右、下、左、上の行動をとった際のQ値を格納している
        self.Q = [0,0,0,0,0]


def main():
    #地図の取得
    maze = np.loadtxt('task4.txt', dtype=int)
    length = len(maze)

    #テキストファイルを元にノードを作成
    maze_node = [[Node(i, j) for j in range(length)] for i in range(length)]

    #壁か否か
    for j in range(length):
        for i in range(length):
            if maze[i][j] == 0:
                maze_node[i][j].wall = False

    #行動選択
    dx_dy = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]
    #行動回数(停止も含める)
    count = 0
    #ハイパーパラメータ
    gamma = 0.9
    alpha = 0.1
    L = 100

    for l in range(L):
    #初期位置
        target = maze_node[1][1]
        #ゴールにたどり着くまで
        while target != maze_node[length-2][length-2]:
            count += 1
            #0.8の確率で思い通りの行動
            #思い通りの行動ができないときは移動しないので処理は記述しない
            random_action = random.random()
            if random_action < 0.8:
                for i in range(5):
                    a = dx_dy[i]
                    nextTarget = maze_node[target.x + a[0]][target.y + a[1]]
                    next_maxQ = max(nextTarget.Q)
                    if nextTarget.wall:
                        td_error = (-1 + gamma * next_maxQ) - target.Q[i]
                        target.Q[i] += alpha * td_error
                    else:
                        if nextTarget == maze_node[length-2][length-2]:
                            td_error = (10 + gamma * next_maxQ) - target.Q[i]
                            target.Q[i] += alpha * td_error
                        else:
                            td_error = (0 + gamma * next_maxQ) - target.Q[i]
                            target.Q[i] += alpha * td_error
                random_action = random.random()
                a = random.choice(dx_dy)
                nextTarget = maze_node[target.x + a[0]][target.y + a[1]]
                if nextTarget.wall != True:
                    target = nextTarget



    Q_table = [[max(maze_node[i][j].Q) for j in range(length)] for i in range(length)]
    # 地図の下準備
    # plt.imshow(maze, cmap="binary")
    plt.figure()
    plt.xticks(np.arange(length), np.arange(length))
    plt.yticks(np.arange(length), np.arange(length))
    plt.plot(1, 1, "D", color="tab:red", markersize=10)
    plt.plot(length - 2, length - 2, "D", color="tab:green", markersize=10)
    plt.imshow(Q_table, cmap="Greens")

    # plt.figure()
    # dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # Q_target = [1, 1]
    # while Q_target != [length - 2, length - 2]:
    #     const = Q_table[Q_target[0]][Q_target[1]]
    #     next_x, next_y = 0, 0
    #     for i in range(4):
    #         nx, ny = Q_target[0] + dx_dy[i][0], Q_target[1] + dx_dy[i][1]
    #         if Q_table[nx][ny] >= const:
    #             const = Q_table[nx][ny]
    #             next_x, next_y = nx, ny
    #     plt.quiver(Q_target[1], Q_target[0], next_y - (Q_target[1]), next_x - (Q_target[0]), angles='xy', scale_units='xy', scale=1)
    #     Q_target = Q_table[next_x][next_y]


    plt.show()





if __name__ == "__main__":
    main()
