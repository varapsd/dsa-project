import time

# dfs algorigthm 
from collections import deque

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def isValid(mat, visited, row, col):
	return (row >= 0) and (row < M) and (col >= 0) and (col < N) \
		   and mat[row][col] == 1 and not visited[row][col]
def BFS(mat, i, j, x, y):
	visited = [[False for x in range(N)] for y in range(M)]
	q = deque()
	visited[i][j] = True
	q.append((i, j, 0))
	min_dist = float('inf')
	while q:
		(i, j, dist) = q.popleft()
		if i == x and j == y:
			min_dist = dist
			break
		for k in range(4):
			if isValid(mat, visited, i + row[k], j + col[k]):
				visited[i + row[k]][j + col[k]] = True
				q.append((i + row[k], j + col[k], dist + 1))

	if min_dist != float('inf'):
		print("The shortest path from source to destination with bfs has length", min_dist)
	else:
		print("Destination can't be reached from given source")


# dfs algorigthm

def isSafe(mat, visited, x, y):
        return not (mat[x][y] == 0 or visited[x][y])


def isValid1(x, y):
        return M > x >= 0 and N > y >= 0

def findShortestPath(mat, visited, i, j, x, y, min_dist, dist):
        if i == x and j == y:
                return min(dist, min_dist)

        visited[i][j] = 1
        if isValid1(i + 1, j) and isSafe(mat, visited, i + 1, j):
                min_dist = findShortestPath(mat, visited, i + 1, j, x, y, min_dist, dist + 1)

        if isValid1(i, j + 1) and isSafe(mat, visited, i, j + 1):
                min_dist = findShortestPath(mat, visited, i, j + 1, x, y, min_dist, dist + 1)

        if isValid1(i - 1, j) and isSafe(mat, visited, i - 1, j):
                min_dist = findShortestPath(mat, visited, i - 1, j, x, y, min_dist, dist + 1)

        if isValid1(i, j - 1) and isSafe(mat, visited, i, j - 1):
                min_dist = findShortestPath(mat, visited, i, j - 1, x, y, min_dist, dist + 1)

        visited[i][j] = 0

        return min_dist


#a star algorithm

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)
            children.append(new_node)
        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

if __name__ == '__main__':

    mat = []
    
    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        for node in line.split(' '):
            adjacentVertices.append(int(node))
        mat.append(adjacentVertices)
    file.close()
    print("----------- input maze 1 -----------------------")
    print("---- mage ----")
    print("")
    print(" ",end="")
    for i in range(len(mat[0])):
        print("_",end="")
    print("")
    for i in range(len(mat)):
        if(i!=0):
            print("|",end="")
        else:
            print(" ",end="")
        for j in range(len(mat[i])):
            if(mat[i][j]==1):
                print(" ",end="")
            else:
                print("#",end="")
        if(i==len(mat[0])-1):
            print(" ")
        else:
            print("|")
    print(" ",end="")
    for i in range(len(mat[0])):
        print("-",end="")
    print("")
    print("--------mage-----------")
    print("")
    M = N = 10
    print("----------BFS algorithm----------")
    print("")
    file1_bfs_start = time.time()
    BFS(mat, 0, 0, 9, 9)
    file1_bfs_end = time.time()
    file1_bfs_time = file1_bfs_end - file1_bfs_start
    print("execution of time file1 on bfs : ", file1_bfs_time)
    # construct a matrix to keep track of visited cells
    print("")
    print("--------- DFS algorithm -------------")
    print("")
    visited = [[0 for x in range(N)] for y in range(M)]
    file1_dfs_start = time.time()

    min_dist = findShortestPath(mat, visited, 0, 0, 9, 9, float('inf'), 0)

    if min_dist != float('inf'):
         print("The shortest path from source to destination with dfs recursive has length", min_dist)
    else:
         print("Destination can't be reached from source")
    file1_dfs_end = time.time()
    file1_dfs_time = file1_dfs_end - file1_dfs_start
    print("execution time of file1 on dfs : ",file1_dfs_time)
    
    # A * algorithm 
    maze = [[0 for i in range(len(mat))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                maze[i][j] = 1

    start = (0, 0)
    end = (9, 9)
    file1_astar_start = time.time()
    
    path = astar(maze, start, end)
    file1_astar_end = time.time()
    file1_astar_time = file1_astar_end - file1_astar_start
    print("")
    print("-------------A* algorithm --------------")
    print("")
    print("execution time of file on A* : ",file1_astar_time)
    print("")
    
    mat = []
    file=open('input1.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        for node in line.split(' '):
            adjacentVertices.append(int(node))
        mat.append(adjacentVertices)
    file.close()
    print("----------- input maze 2 -----------------------")
    print("---- mage ----")
    print("")
    print(" ",end="")
    for i in range(len(mat[0])):
        print("_",end="")
    print("")
    for i in range(len(mat)):
        if(i!=0):
            print("|",end="")
        else:
            print(" ",end="")
        for j in range(len(mat[i])):
            if(mat[i][j]==1):
                print(" ",end="")
            else:
                print("#",end="")
        if(i==len(mat[0])-1):
            print(" ")
        else:
            print("|")
    print(" ",end="")
    for i in range(len(mat[0])):
        print("-",end="")
    print("")
    print("--------mage-----------")
    print("")
    M = N = 10
    print("----------BFS algorithm----------")
    print("")
    file2_bfs_start = time.time()
    BFS(mat, 0, 0, 9, 9)
    file2_bfs_end = time.time()
    file2_bfs_time = file2_bfs_end - file2_bfs_start
    print("execution of time file1 on bfs : ", file2_bfs_time)
    # construct a matrix to keep track of visited cells
    print("")
    print("--------- DFS algorithm -------------")
    print("")
    visited = [[0 for x in range(N)] for y in range(M)]
    file2_dfs_start = time.time()

    min_dist = findShortestPath(mat, visited, 0, 0, 9, 9, float('inf'), 0)

    if min_dist != float('inf'):
         print("The shortest path from source to destination with dfs recursive has length", min_dist)
    else:
         print("Destination can't be reached from source")
    file2_dfs_end = time.time()
    file2_dfs_time = file2_dfs_end - file2_dfs_start
    print("execution time of file1 on dfs : ",file2_dfs_time)
    
    # A * algorithm 
    maze = [[0 for i in range(len(mat))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                maze[i][j] = 1

    start = (0, 0)
    end = (9, 9)
    file2_astar_start = time.time()
    
    path = astar(maze, start, end)
    file2_astar_end = time.time()
    file2_astar_time = file2_astar_end - file2_astar_start
    print("")
    print("-------------A* algorithm --------------")
    print("")
    print("execution time of file on A* : ",file2_astar_time)
    print("")
    
    mat = []
    file=open('input3.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        for node in line.split(' '):
            adjacentVertices.append(int(node))
        mat.append(adjacentVertices)
    file.close()
    print("----------- input maze 3 -----------------------")
    print("---- mage ----")
    print("")
    print(" ",end="")
    for i in range(len(mat[0])):
        print("_",end="")
    print("")
    for i in range(len(mat)):
        if(i!=0):
            print("|",end="")
        else:
            print(" ",end="")
        for j in range(len(mat[i])):
            if(mat[i][j]==1):
                print(" ",end="")
            else:
                print("#",end="")
        if(i==len(mat[0])-1):
            print(" ")
        else:
            print("|")
    print(" ",end="")
    for i in range(len(mat[0])):
        print("-",end="")
    print("")
    print("--------mage-----------")
    print("")
    M = N = 10
    print("----------BFS algorithm----------")
    print("")
    file3_bfs_start = time.time()
    BFS(mat, 0, 0, 9, 9)
    file3_bfs_end = time.time()
    file3_bfs_time = file3_bfs_end - file3_bfs_start
    print("execution of time file1 on bfs : ", file3_bfs_time)
    # construct a matrix to keep track of visited cells
    print("")
    print("--------- DFS algorithm -------------")
    print("")
    visited = [[0 for x in range(N)] for y in range(M)]
    file3_dfs_start = time.time()

    min_dist = findShortestPath(mat, visited, 0, 0, 9, 9, float('inf'), 0)

    if min_dist != float('inf'):
         print("The shortest path from source to destination with dfs recursive has length", min_dist)
    else:
         print("Destination can't be reached from source")
    file3_dfs_end = time.time()
    file3_dfs_time = file3_dfs_end - file3_dfs_start
    print("execution time of file1 on dfs : ",file3_dfs_time)
    
    # A * algorithm 
    maze = [[0 for i in range(len(mat))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                maze[i][j] = 1

    start = (0, 0)
    end = (9, 9)
    file3_astar_start = time.time()
    
    path = astar(maze, start, end)
    file3_astar_end = time.time()
    file3_astar_time = file3_astar_end - file3_astar_start
    print("")
    print("-------------A* algorithm --------------")
    print("")
    print("execution time of file on A* : ",file3_astar_time)
    print("")
    
    mat = []
    file=open('input4.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        for node in line.split(' '):
            adjacentVertices.append(int(node))
        mat.append(adjacentVertices)
    file.close()
    print("----------- input maze 4 -----------------------")
    print("---- mage ----")
    print("")
    print(" ",end="")
    for i in range(len(mat[0])):
        print("_",end="")
    print("")
    for i in range(len(mat)):
        if(i!=0):
            print("|",end="")
        else:
            print(" ",end="")
        for j in range(len(mat[i])):
            if(mat[i][j]==1):
                print(" ",end="")
            else:
                print("#",end="")
        if(i==len(mat[0])-1):
            print(" ")
        else:
            print("|")
    print(" ",end="")
    for i in range(len(mat[0])):
        print("-",end="")
    print("")
    print("--------mage-----------")
    print("")
    M = N = 10
    print("----------BFS algorithm----------")
    print("")
    file4_bfs_start = time.time()
    BFS(mat, 0, 0, 9, 9)
    file4_bfs_end = time.time()
    file4_bfs_time = file4_bfs_end - file4_bfs_start
    print("execution of time file1 on bfs : ", file2_bfs_time)
    # construct a matrix to keep track of visited cells
    print("")
    print("--------- DFS algorithm -------------")
    print("")
    visited = [[0 for x in range(N)] for y in range(M)]
    file4_dfs_start = time.time()

    min_dist = findShortestPath(mat, visited, 0, 0, 9, 9, float('inf'), 0)

    if min_dist != float('inf'):
         print("The shortest path from source to destination with dfs recursive has length", min_dist)
    else:
         print("Destination can't be reached from source")
    file4_dfs_end = time.time()
    file4_dfs_time = file4_dfs_end - file4_dfs_start
    print("execution time of file1 on dfs : ",file4_dfs_time)
    
    # A * algorithm 
    maze = [[0 for i in range(len(mat))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                maze[i][j] = 1

    start = (0, 0)
    end = (9, 9)
    file4_astar_start = time.time()
    
    path = astar(maze, start, end)
    file4_astar_end = time.time()
    file4_astar_time = file4_astar_end - file4_astar_start
    print("")
    print("-------------A* algorithm --------------")
    print("")
    print("execution time of file on A* : ",file4_astar_time)
    print("")

    print("---------Analysis-------------")
    print("file\tdfs\tbfs\tA*")
    print("file1\t",file1_dfs_time,"\t",file1_bfs_time,"\t",file1_astar_time)
    print("file2\t",file2_dfs_time,"\t",file2_bfs_time,"\t",file2_astar_time)
    print("file3\t",file3_dfs_time,"\t",file3_bfs_time,"\t",file3_astar_time)
    print("file4\t",file4_dfs_time,"\t",file4_bfs_time,"\t",file4_astar_time)
