import numpy as np


def main():
    maze = np.loadtxt('task2.txt', dtype=int)
    maze[1][1] = 1
    hight = maze.shape[0]-1
    width = maze.shape[1]-1
    goal_x = hight-1
    goal_y = width-1
    openlist = [[1,1]]
    closed = []
    dx_dy = [[1,0],[0,1],[-1,0],[0,-1]]


    while openlist:
        target = openlist.pop()
        print("target",target,"\n")
        closed.append(target)
        if target[0] == goal_x and target[1] == goal_y:
            break
        for i in range(4):
            nx, ny = target[0] + dx_dy[i][0], target[1] + dx_dy[i][1]
            if 1 <= nx < hight and 1 <= ny < width and maze[nx][ny] == 0:
                openlist.append([nx, ny])
                maze[nx][ny] = 1


    print("探索結果")
    print(closed)

if __name__ == "__main__":
    main()
