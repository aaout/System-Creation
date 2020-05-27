import matplotlib.pyplot as plt
import numpy as np


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    maze = np.loadtxt('task3.txt', dtype=int)
    length = len(maze)
    maze_node = []
    openlist = [Node(1, 1)]
    closedlist = []
    dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    #地図の下準備
    plt.imshow(maze, cmap="binary")
    # plt.xticks(rotation=90)
    plt.xticks(np.arange(length), np.arange(length))
    plt.yticks(np.arange(length), np.arange(length))
    plt.plot(1, 1, "D", color="tab:red", markersize=10)
    plt.plot(length-2, length-2, "D", color="tab:green", markersize=10)

    # 図と最終的なクローズドリストの表示
    plt.show()


    while openlist:
        target = openlist.pop()
        closedlist.append(target)

        for i in range(4):
            nx, ny = target.x + dx_dy[i][0], target.y + dx_dy[i][1]
            if maze[nx][ny] == 0:
                openlist.append(Node(nx,ny))



    length = len(maze)
    for y in range(length):
        for x in range(length):
            if maze[y][x] == 0:
                maze_node.append(Node(x,y))
    target = maze_node.pop()
    print(length)

if __name__ == "__main__":
    main()
