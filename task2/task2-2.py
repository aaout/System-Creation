#キューを作成するため導入
from collections import deque

import matplotlib.pyplot as plt
import numpy as np


def main():
    #地図の取得
    maze = np.loadtxt('task2.txt', dtype=int)

    #地図の縦と横の長さ
    height = maze.shape[0]-1
    width = maze.shape[1] - 1

    #ゴールは一マス内側
    goal_x = height-1
    goal_y = width - 1

    #各リストの作成
    #オープンリストをキューで作成
    openlist = deque([[1,1]])
    closed = []
    dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    #地図の下準備
    plt.imshow(maze, cmap="binary")
    plt.xticks(rotation=90)
    plt.xticks(np.arange(width), np.arange(width))
    plt.yticks(np.arange(height), np.arange(height))
    plt.plot(1, 1, "D", color="tab:red", markersize=10)
    plt.plot(goal_x, goal_y, "D", color="tab:green", markersize=10)
    maze[1][1] = 1

    #オープンリストが空になるまで
    while openlist:
        #注目しているマス目
        target = openlist.popleft()
        closed.append(target)

        #ゴールに着いたら終わり
        if target[0] == goal_x and target[1] == goal_y:
            break
        for i in range(4):
            #注目マスの前後左右を探索
            #未チェックマスならチェックしてオープンリストに追加
            #ついでにベクトルもここでプロットしておく
            nx, ny = target[0] + dx_dy[i][0], target[1] + dx_dy[i][1]
            if 1 <= nx < height and 1 <= ny < width and maze[nx][ny] == 0:
                openlist.append([nx, ny])
                plt.quiver(target[1], target[0], ny-target[1], nx-target[0], angles='xy', scale_units='xy', scale=1)
                maze[nx][ny] = 1

    #図と最終的なクローズドリストの表示
    plt.show()
    print("探索結果")
    print(closed)

if __name__ == "__main__":
    main()
