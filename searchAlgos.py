# -*- coding: utf-8 -*-
"""
@author: MortZ

Search algorithms
"""

from Npuzzle import *


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