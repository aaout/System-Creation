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

    #地図の下準備
    # plt.imshow(maze, cmap="binary")
    # plt.xticks(np.arange(length), np.arange(length))
    # plt.yticks(np.arange(length), np.arange(length))
    # plt.plot(1, 1, "D", color="tab:red", markersize=10)
    # plt.plot(length - 2, length - 2, "D", color="tab:green", markersize=10)

    #初期位置
    target = maze_node[1][1]
    #行動選択
    dx_dy = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]
    #報酬
    reward = 0
    #行動回数(停止も含める)
    count = 0

    #ゴールにたどり着くまで
    while target != maze_node[length-2][length-2]:
        count += 1
        #0.8の確率で思い通りの行動
        #思い通りの行動ができないときは移動しないので処理は記述しない
        random_action = random.random()
        if random_action < 0.8:
            a = random.choice(dx_dy)
            nextTarget = maze_node[target.x + a[0]][target.y + a[1]]
            if nextTarget.wall:
                reward -= 1
            else:
                target = nextTarget

    #ゴールにたどり着いたら報酬追加
    reward += 10

    #行動回数と報酬を出力
    print("reward:", reward)
    print("count:",count)


if __name__ == "__main__":
    main()
