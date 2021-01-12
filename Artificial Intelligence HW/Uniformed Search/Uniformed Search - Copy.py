import queue


# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of 1s and 0s
def readGrid(filename):
    # print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])

    f.close()
    # print 'Exiting readGrid'
    return grid


# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, path):
    # print('In outputGrid')
    filenameStr = 'path.txt'

    # Open filename
    f = open(filenameStr, 'w')

    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path) - 1:
            grid[p[0]][p[1]] = '*'

    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):

            # Don't add a ' ' at the end of a line
            if c < len(row) - 1:
                f.write(str(col) + ' ')
            else:
                f.write(str(col))

        # Don't add a '\n' after the last line
        if r < len(grid) - 1:
            f.write("\n")

    # Close file
    f.close()
    # print('Exiting outputGrid')


class Node:

    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent

    def say_value(self):
        return [self.value[0], self.value[1]]


def uninformedSearch(grid, start, goal):
    """
    Initialize a Node object called ‘current’ to track which node the agent is currently at.
    Initialize a data structure to hold the open list.
    Initialize a data structure to hold the closed list.
    Create a while loop with a proper termination condition. This while loop will contain the searching actions.
    """
    openList = queue.LifoQueue()
    openListCopy = []
    closedList = []
    numExpanded = 0
    path = []

    current = Node([start[0], start[1]], None)
    openList.put(current)
    openListCopy.append(current)
    print('test', closedList)

    while not (current.value is goal):
        if openList.empty():
            path = False
            return path

        current = openList.get()

        # test
        print('CURRENT', current.value)
        for i in openListCopy:
            print(i.value)
        if current.value == goal:
            path = setPath(current, path, start)
            return path

        closedList.append(current)

        expandNode(current, openList, openListCopy, closedList, grid)

        numExpanded += 1


def getNeighbors(current, grid):
    """
    The ‘location’ parameter should be a 2-element list that describes a location, such as [1,1], [1,2], etc.
    The ‘grid’ parameter is the 2D list of 1’s and 0’s representing a grid.

    The function should return a list of positions (e.g., [[1,3], [2,1], [2,2]]) that
    1) are adjacent to the ‘location’ parameter,
    2) have a value of 0 on the grid, and
    3) are within the grid boundaries.
    """
    a, b = current

    neighbors = []
    if grid[a][b - 1] != 1:  # left
        neighbors.append([a, b - 1])
    if grid[a][b + 1] != 1:  # right
        neighbors.append([a, b + 1])
    if grid[a + 1][b] != 1:  # up
        neighbors.append([a + 1, b])
    if grid[a - 1][b] != 1:  # down
        neighbors.append([a - 1, b])
    return neighbors


def expandNode(node, openList, openListCopy, closedList, grid):
    """
    Create a function called expandNode that takes in at least a Node object (it may
    take in more parameters depending on your preference). The purpose of this function is
    to get all the neighbors of the Node object passed in and add those neighbors to the
    open list if and only if the necessary conditions are passed.
    """
    neighbors = getNeighbors(node.value, grid)

    for n in neighbors:
        nd = Node(n, node)

        if not InList(nd, closedList) and not InList(nd, openListCopy):
            openList.put(nd)
            openListCopy.append(nd)


def InList(nd, aList):
    for i in aList:
        if i.value == nd.value:  # Value checking prevents duplication
            return True
        else:
            return False


def setPath(current, path, start):
    pathCost = 0
    x = current
    while x.parent is not None:
        path.append(x.value)
        x = x.parent  # x.parent works like a linked list and creates the path
        pathCost += 1
    path.append([start[0], start[1]])
    print('Path Cost is', pathCost)
    return path


def main():
    """
    Create a main function and set up your script to call it when executed.
    In the main function, call readGrid to read a file with a grid into a 2D list of 1’s and 0’s.
    Create list variables to hold the start and goal locations.
    Then call the function that implements the searching algorithm.
    """
    grid = readGrid('path.txt')
    start = [1, 1]
    goal = [1, 5]
    path = uninformedSearch(grid, start, goal)
    if path is False:
        print('Failure. Route not found.')
    else:
        outputGrid(grid, start, goal, path)

main()
