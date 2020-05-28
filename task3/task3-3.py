import matplotlib.pyplot as plt
import numpy as np


#ノードの状態を確保するクラスを作成
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wall = True
        self.check = False
        self.g = 0
        self.h = 30 - x - y


def main():
    #地図の取得
    maze = np.loadtxt('task3.txt', dtype=int)
    length = len(maze)

    #各リストの作成
    openlist = []
    closedlist = []
    #テキストファイルを元にノードを作成
    maze_node = [[Node(i, j) for j in range(length)] for i in range(length)]
    dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    #壁か否か
    for j in range(length):
        for i in range(length):
            if maze[i][j] == 0:
                maze_node[i][j].wall = False
    openlist.append(maze_node[1][1])
    maze_node[1][1].check = True

    #地図の下準備
    plt.imshow(maze, cmap="binary")
    plt.xticks(np.arange(length), np.arange(length))
    plt.yticks(np.arange(length), np.arange(length))
    plt.plot(1, 1, "D", color="tab:red", markersize=10)
    plt.plot(length - 2, length - 2, "D", color="tab:green", markersize=10)


    #オープンリストが空になるまで
    while openlist:
        # for i in openlist:
        #     print(i.x, i.y, i.g)
        # print("\n")
        #注目しているマス目
        target = openlist.pop(0)
        closedlist.append(target)

        #ゴールに着いたら終わり
        #注目マスの前後左右を探索
        #未チェックマスならチェックしてオープンリストに追加
        #ついでにベクトルもここでプロットしておく
        if (target.x) == length - 2 and (target.y) == length - 2:
            break
        for i in range(4):
            nx, ny = target.x + dx_dy[i][0], target.y + dx_dy[i][1]
            #範囲内の道で未チェックであるもの
            if maze_node[nx][ny].wall == False and maze_node[nx][ny].check == False and 1 <= nx < (length - 1) and 1 <= ny < (length - 1):
                #条件を満たすノードはとりあえずリストの右端に代入
                #各ノードのパラメータを更新
                #チェックを付け、コストをインクリメントする
                openlist.append(maze_node[nx][ny])
                maze_node[nx][ny].check = True
                maze_node[nx][ny].g = target.g + 1
                plt.quiver(target.y, target.x, ny - (target.y), nx - (target.x), angles='xy', scale_units='xy', scale=1)


                #ソート部分
                #先ほど代入したノードに関してバブルソートを行い、左側に小さいものがくるようにする
                var = len(openlist) - 1
                while var > 0:
                    if openlist[var].g < openlist[var-1].g:
                        openlist[var], openlist[var - 1] = openlist[var - 1], openlist[var]
                        var -= 1
                    else:
                        break


    #図と最終的なクローズドリストの表示
    plt.show()

if __name__ == "__main__":
    main()
