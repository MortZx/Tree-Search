# Foundations of AI coursework
# Implement BFS, DFS, IDS & A* to search N-puzzle
# Mortimer Sotom
# Southampton University
# Student ID: 29875056


import random


# attributes or information of each node
class Node:
    def __init__(self, state, parent, move_operator, depth):
        # node state
        self.state = state
        # parent node
        self.parent = parent
        # move operator to get to that node
        self.move_operator = move_operator
        # node depth
        self.depth = depth
        # heuristic evaluation value
        self.eval = evaluation(self.depth, self.state)


# Prints the state of the board in a human friendly readable form
def display_board_state(state):
    print("---------------------")
    print("| %i | %i | %i | %1 |" % (state[0], state[1], state[2], state[3]))
    print("---------------------")
    print("| %i | %i | %i | %1 |" % (state[4], state[5], state[6], state[7]))
    print("---------------------")
    print("| %i | %i | %i | %1 |" % (state[8], state[9], state[10], state[11]))
    print("---------------------")
    print("| %i | %i | %i | %1 |" % (state[12], state[13], state[14], state[15]))
    print("---------------------")


# Check if the goal state has been reached
def check_goal(state):
    # index: [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    # Depending on the start state, change the if statements to match the required goal state
    if state[5] == 2 and state[9] == 3 and state[13] == 4:
        return True
    return False


# expand a node and returns the successors moves) in a random order
def expand_node_rand(node, states_visited):
    expanded_nodes = expand_node(node, states_visited)
    random.shuffle(expanded_nodes)
    return expanded_nodes


# expand a node
# return a list of the successor nodes
def expand_node(node, states_visited):
    # creates the list to be returned
    # all moves are considered each time a node is expanded
    # all information of the node class is passed for each node generated (state, class, move operator, depth
    successors = [gen_node(move_up(node.state), node, "UP ", node.depth + 1),
                      gen_node(move_down(node.state), node, "DOWN", node.depth + 1),
                      gen_node(move_left(node.state), node, "LEFT", node.depth + 1),
                      gen_node(move_right(node.state), node, "RIGHT", node.depth + 1)]

    # iterate through the list using Python list comprehension and removes the successors which are impossible
    # by identifying the node lists which have None
    successors = [node for node in successors if node.state is not None]
    # same principle applied to previously visited states for graph search
    successors = [node for node in successors if node.state not in states_visited]
    return successors


# generate a new node with all of its information
def gen_node(state, parent, operator, depth):
    return Node(state, parent, operator, depth)


# Next 4 functions are used when expanding nodes.
# Passes state of node being expanded, checks if move is possible
# returns state of move in a list or None if not possible


# Moves the agent up one tile
# returns the new state in a list
def move_up(state):
    # Copy the current board state
    new = state[:]
    index = new.index(0)

    # Check if the agent is on the upper side of the board (cant move up)
    if index not in [0, 1, 2, 3]:
        # Swap the values.
        temp = new[index - 4]
        new[index - 4] = new[index]
        new[index] = temp
        return new

    else:
        return None


# Moves the agent down one tile
# returns the new state in a list
def move_down(state):
    # Copy the current board state
    new = state[:]
    index = new.index(0)

    # Check if the agent is on the lower side of the board (cant move down)
    if index not in [12, 13, 14, 15]:
        # Swap the values.
        temp = new[index + 4]
        new[index + 4] = new[index]
        new[index] = temp
        return new

    else:
        return None


# Moves the agent left one tile
# returns the new state in a list
def move_left(state):
    # Copy the current board state
    new = state[:]
    index = new.index(0)

    # Check if the agent is on the left side of the board (cant move left)
    if index not in [0, 4, 8, 12]:
        # update the state element values
        temp = new[index - 1]
        new[index - 1] = new[index]
        new[index] = temp
        return new

    else:
        return None


# Moves the agent right one tile
# returns the new state in a list
def move_right(state):
    # Copy the current board state
    new = state[:]
    index = new.index(0)

    # Check if the agent is on the right side of the board (cant move right)
    if index not in [3, 7, 11, 15]:
        # update the state element values
        temp = new[index + 1]
        new[index + 1] = new[index]
        new[index] = temp
        return new

    else:
        return None


# BFS alg to find goal state
# can return the path, states or move operators for the solution.
def bfs(start):
    print("BFS start")
    # Initialise variables
    number_nodes_expanded = 0
    states_visited = []
    # Initialise the fringe with the start state
    fringe = [gen_node(start, None, None, 0)]

    # BFS until solution is found or fringe is empty
    while len(fringe) is not 0:
        # prepare to expand the first node in the fringe --> FIFO queue
        node = fringe.pop(0)
        # update the states visited list
        states_visited.append(node.state)

        # check if the node is in goal state before expanding
        if check_goal(node.state) is True:
            # Initialise variable to print the solution
            operator = []
            path = []
            temp = node

            # Iterate from the goal node up the parent nodes while storing the path, state and move operator
            while True:
                operator.insert(0, temp.move_operator)
                path.insert(0, temp.state)
                if temp.depth == 1:
                    break
                temp = temp.parent

            # Print all the stored variables to print the solution
            print("number of fringe left in fringe/queue = ", len(fringe))
            print("number of fringe expanded = ", number_nodes_expanded)
            for i in range(len(operator)):
                print("move[",i,"]: ", operator[i], "\t state: ", path[i])
                display_board_state(path[i])

            # can return any of the solution variables
            return path

        # expand the node and the successors to the front of the fringe --> FIFO queue
        # use expand_node to return successors in default order
        # use expand_node_rand to return ^ in random order
        # last argument is states_visited to implement graph search or [] for standard alg
        fringe.extend(expand_node(node, states_visited))

        # update the number of expanded nodes
        number_nodes_expanded += 1
        if number_nodes_expanded % 100000 == 0:
            print("number of expanded fringe :", number_nodes_expanded)


# DFS alg to find goal state
# can return the path, states or move operators for the solution.
def dfs(start, depth):
    print("DFS start")
    # Initialise variables
    number_nodes_expanded = 0
    states_visited = []
    depth_limit = depth
    # Initialise the fringe with the start state
    fringe = [gen_node(start, None, None, 0)]

    # DFS until solution is found or fringe is empty
    while len(fringe) is not 0:
        # prepare to expand the first node in the fringe --> LIFO queue
        node = fringe.pop(0)
        # update the states visited list
        states_visited.append(node.state)

        # check if the node is in goal state before expanding
        if check_goal(node.state) is True:
            # Initialise variable to print the solution
            operator = []
            path = []
            temp = node

            # Iterate from the goal node up the parent nodes while storing the path, state and move operator
            while True:
                operator.insert(0, temp.move_operator)
                path.insert(0, temp.state)
                if temp.depth <= 1:
                    break
                temp = temp.parent

            # Print all the stored variables to print the solution
            for i in range(len(operator)):
                print("move[", i + 1, "]: ", operator[i], "\t state: ", path[i])
                display_board_state(path[i])
            print("number of fringe left in fringe/queue = ", len(fringe))
            print("number of fringe expanded = ", number_nodes_expanded)
            print("depth = ", node.depth)
            print("DFS end")

            # can return any of the solution variables
            return path

            # check if the depth limit is reached
        if node.depth < depth_limit:
            # expand the node and the successors to the end of the fringe --> LIFO queue
            # use expand_node to return successors in default order !! only if using with graph search or endless loop
            # use expand_node_rand to return ^ in random order
            # last argument is states_visited to implement graph search or [] for standard alg

            # fringe.extend(expand_node_rand(node, []))
            expanded_nodes = expand_node_rand(node, [])
            expanded_nodes.extend(fringe)
            fringe = expanded_nodes

            # update number of nodes expanded
            number_nodes_expanded += 1
            if number_nodes_expanded % 100000 == 0:
                print("number of expanded fringe :", number_nodes_expanded)


# IDS alg to find goal state
# can return the path, states or move operators for the solution.
# calls DFS with incremental depth
def ids(start, depth=50):
    print("IDS start")
    for i in range(depth):
        print("\nIDS with depth ... ", i)
        result = dfs(start, i)
        print("result is: ", result)
        if result is not None:
            return result
    print("IDS end")


# A* alg to find goal state
# can return the path, states or move operators for the solution.
def a_star(start):
    print("A* start (Manhattan distance)")
    # Initialise variables
    fringe = [gen_node(start, None, None, 0)]
    number_nodes_expanded = 0
    states_visited = []

    # BFS until solution is found or fringe is empty
    while len(fringe) is not 0:

        # after first expansion, sort fringe with evaluation values
        if number_nodes_expanded > 1:
            fringe.sort(key=lambda x: x.eval)

        # prepare to expand the next node in the fringe --> FIFO queue
        node = fringe.pop(0)
        # update the states visited list
        states_visited.append(node.state)

        # check if the node is in goal state before expanding
        if check_goal(node.state) is True:
            # Initialise variable to print the solution
            operator = []
            path = []
            temp = node

            # Iterate from the goal node up the parent nodes while storing the path, state and move operator
            while True:
                operator.insert(0, temp.move_operator)
                path.insert(0, temp.state)
                if temp.depth <= 1:
                    break
                temp = temp.parent

            # Print all the stored variables to print the solution
            for i in range(len(operator)):
                print("move[", i+1, "] = ", operator[i], "\t state: ", path[i])
                display_board_state(path[i])
            print("depth = ", node.depth)
            print("number of fringe expanded = ", number_nodes_expanded)
            print("number of fringe left in fringe/queue = ", len(fringe))
            print("A* end")

            # can return any of the solution variables
            return path

        # expand the node and the successors to the front of the fringe --> FIFO queue
        # last argument is states_visited to implement graph search or [] for standard alg
        fringe.extend(expand_node_rand(node, []))

        # update the number of expanded nodes
        number_nodes_expanded += 1
        if number_nodes_expanded % 100000 == 0:
            print("number of expanded fringe :", number_nodes_expanded)


# heuristic evaluation function
def evaluation(depth, state):
    # f(n) = h(n) + g(n)
    # use misplaced_tiles or manhattan
    return depth + manhattan(state)


# evaluation function for Manhattan distance
def manhattan(state):
    if state is None:
        return 1000         # return large value in case it is used

    # Initialise distance
    dist = 0

    # Due to 1D index, Manhattan dist is calculate with if functions.
    # comment or uncomment the relevant sections depending on the start and goal state (number of non white tiles)
    for i in range(len(state)):
        if state[i] is 2:
            if i in range(0, 4):
                dist = dist + 1 + abs(i-1)
            if i in range(4, 8):
                dist = dist + abs(i-5)
            if i in range(8, 12):
                dist = dist + 1 + abs(i-9)
            if i in range(12, 16):
                dist = dist + 2 + abs(i-13)

        if state[i] is 3:
            if i in range(0, 4):
                dist = dist + 2 + abs(i-1)
            if i in range(4, 8):
                dist = dist + 1 + abs(i-5)
            if i in range(8, 12):
                dist = dist + abs(i-9)
            if i in range(12, 16):
                dist = dist + 1 + abs(i-13)

        if state[i] is 4:
            if i in range(0, 4):
                dist = dist + 3 + abs(i-1)
            if i in range(4, 8):
                dist = dist + 2 + abs(i-5)
            if i in range(8, 12):
                dist = dist + 1 + abs(i-9)
            if i in range(12, 16):
                dist = dist + abs(i-13)

    return dist


# evaluation function for the number of misplaced tiles
def misplaced_tiles(state):
    # counts number of misplaced tiles
    # [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    if state is None:
        return 100          # large value in case it is used

    # comment or uncomment relevant sections depending on which tiles are used
    misplaced = 0
    if state[0] is not 1 and state[0] is not 0: misplaced += 1
    if state[1] is not 1 and state[1] is not 0: misplaced += 1
    if state[2] is not 1 and state[2] is not 0: misplaced += 1
    if state[3] is not 1 and state[3] is not 0: misplaced += 1
    if state[4] is not 1 and state[0] is not 0: misplaced += 1
    if state[5] is not 2: misplaced += 1
    if state[6] is not 1 and state[6] is not 0: misplaced += 1
    if state[7] is not 1 and state[0] is not 0: misplaced += 1
    if state[8] is not 1 and state[8] is not 0: misplaced += 1
    if state[9] is not 3: misplaced += 1
    if state[10] is not 1 and state[0] is not 0: misplaced += 1
    if state[11] is not 1 and state[0] is not 0: misplaced += 1
    if state[12] is not 1 and state[0] is not 0: misplaced += 1
    if state[13] is not 4: misplaced += 1
    if state[14] is not 1 and state[0] is not 0: misplaced += 1
    if state[15] is not 1 and state[0] is not 0: misplaced += 1

    return misplaced


# A python-isim. Basically if the file is being run execute the main() function.
if __name__ == "__main__":
    starting_state = [1, 1, 1, 1,
                      1, 1, 1, 1,
                      1, 1, 1, 1,
                      2, 3, 4, 0]

    # call the desired alg
    result = a_star(starting_state)

    if result is None:
        print("No solution found")
    else:
        print("\n\nEND")