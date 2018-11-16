# Foundations of AI coursework
# Implement BFS, DFS, IDS & A* to search N-puzzle
# Mortimer Sotom
# Southampton University
# Student ID: 29875056


import random
from searchAlgos import *

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


# heuristic evaluation function
def evaluation(depth, state):
    # f(n) = h(n) + g(n)
    # use misplaced_tiles or manhattan
    return depth + manhattan(state)



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