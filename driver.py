import sys
import math
import time
import resource
import Queue as QQ
# ------------------------Here are the basic Data Structure we will use.--------------------
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def set(self):
        return len(set(self.items))

# ------------------------Here are the method functions.------------------------
def goalTest(state):
    if state == GOAL:
        return True
    else:
        return False

def board(l, n):
    output = []
    for index in xrange(n):
        output.append(l[n * index : n * (index + 1)])
    return output

def swap_value(state_board_copy, i, ni):
    state_board_copy[i], state_board_copy[ni] = state_board_copy[ni], state_board_copy[i]
    return state_board_copy

def neighbors(index, state):
    neighbor_list = []
    action_list = []
    if index > (n - 1):
        neighbor_list.append(tuple(swap_value(list(state), index, index - 3)))
        action_list.append("Up")

    if index < n * (n - 1):
        neighbor_list.append(tuple(swap_value(list(state), index, index + 3)))
        action_list.append("Down")
        #RIGHT
    if (index % n) != 0:
        neighbor_list.append(tuple(swap_value(list(state), index, index - 1)))
        action_list.append("Left")

    if (index % n) != (n - 1):
        neighbor_list.append(tuple(swap_value(list(state), index, index + 1)))
        action_list.append("Right")

    return neighbor_list, action_list

def neighbors_reverse(index, state):

    neighbor_list = []
    action_list = []

        #RIGHT
    if (index % n) != (n - 1):
        neighbor_list.append(tuple(swap_value(list(state), index, index + 1)))
        action_list.append("Right")
        #LEFT
    if (index % n) != 0:
        neighbor_list.append(tuple(swap_value(list(state), index, index - 1)))
        action_list.append("Left")
        #DOWN
    if index < n * (n - 1):
        neighbor_list.append(tuple(swap_value(list(state), index, index + 3)))
        action_list.append("Down")
        #UP
    if index > (n - 1):
        neighbor_list.append(tuple(swap_value(list(state), index, index - 3)))
        action_list.append("Up")
    return neighbor_list, action_list

def Failure():
    return "cannot find an optimal solution."

def Success(state, max_fringe_size, len_path_to_goal, fringe_size, path_to_goal, nodes_expanded, max_search_depth):
    file = open("output.txt", "w")
    print "path_to_goal: " + str(list(path_to_goal))
    file.write("path_to_goal: " + str(list(path_to_goal)) + "\n")
    print "cost_of_path: " + str(len_path_to_goal)
    file.write("cost_of_path: " + str(len_path_to_goal) + "\n")
    print "nodes_expanded: " + str(nodes_expanded)
    file.write("nodes_expanded: " + str(nodes_expanded) + "\n")
    print "fringe_size: %d\n" % (fringe_size)
    file.write("fringe_size: %d\n" % (fringe_size))
    print "max_fringe_size: %d" % (max_fringe_size)
    file.write("max_fringe_size: %d\n" %(max_fringe_size))
    print "search_depth: %d" % (len_path_to_goal)
    file.write("search_depth: %d\n" % (len_path_to_goal))
    print "max_search_depth: %d" % (max_search_depth)
    file.write("max_search_depth: %d\n" % (max_search_depth))
    print "running_time: %s" % (time.clock() - start_time)
    file.write("running_time: %s\n" % (time.clock() - start_time))
    print "max_ram_usage: %s" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1.0 / (1024 * 1024))
    file.write("max_ram_usage: %s\n" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1.0 / (1024 * 1024)))
    file.close()
    sys.exit()


def BFS_method(initial_state):
    max_fringe_size, max_search_depth, path_to_goal, nodes_expanded = 0, 0, [], 0

    frontier = Queue()
    action = Queue()
    frontier.enqueue(tuple(initial_state))
    action.enqueue(tuple([]))
    explored = set([])
    explored_frontier = set([])
    explored_frontier.add(tuple(initial_state))
    while not frontier.isEmpty():
        state = list(frontier.dequeue())
        explored.add(tuple(state))
        path_to_goal = action.dequeue()

        if goalTest(state):
            return Success(state, max_fringe_size, len(path_to_goal), frontier.size(), path_to_goal, nodes_expanded, max_search_depth)
        index = state.index(0)
        nodes_expanded += 1

        neighbor_list = neighbors(index, state)
        length_neighbor = len(neighbor_list[0])
        for i in xrange(length_neighbor):
            if neighbor_list[0][i] not in explored_frontier:
                explored_frontier.add(neighbor_list[0][i])
                frontier.enqueue(neighbor_list[0][i])
                action.enqueue(path_to_goal + (neighbor_list[1][i],))
                max_search_depth = max(max_search_depth, len(path_to_goal) + 1)
        max_fringe_size = max(max_fringe_size, frontier.size())

    return Failure()

def DFS_method(initial_state):

    max_fringe_size, max_search_depth, path_to_goal, nodes_expanded = 0, 0, [], 0

    frontier = Stack()
    action = Stack()
    frontier.push(tuple(initial_state))
    action.push(tuple([]))
    explored = set([])
    explored_frontier = set([])

    explored_frontier.add(tuple(initial_state))
    while not frontier.isEmpty():
        state = list(frontier.pop())
        explored.add(tuple(state))
        path_to_goal = action.pop()

        if goalTest(state):
            return Success(state, max_fringe_size, len(path_to_goal), frontier.size(), path_to_goal, nodes_expanded, max_search_depth)
        index = state.index(0)
        nodes_expanded += 1

        neighbor_list = neighbors_reverse(index, state)
        length_neighbor = len(neighbor_list[0])
        for i in xrange(length_neighbor):
            if neighbor_list[0][i] not in explored_frontier:
                explored_frontier.add(neighbor_list[0][i])
                frontier.push(neighbor_list[0][i])

                # There is way to do this faster
                # Consider using linked to list to do backtracing.
                # The same to BFS.
                action.push(path_to_goal + (neighbor_list[1][i],))

                max_search_depth = max(max_search_depth, len(path_to_goal) + 1)
        max_fringe_size = max(max_fringe_size, frontier.size())

    return Failure()

def heuristics(state):
    heuristics_value = 0
    for index in xrange(len(state)):
        if state[index] != 0:
            index_row, index_column = index / n, index % n
            item_row, item_column = state[index] / n, state[index] % n
            heuristics_value += abs(index_row - item_row) + abs(index_column - item_column)
    return heuristics_value

def AST_method(initial_state):
    # print initial_state
    max_fringe_size, max_search_depth, path_to_goal, nodes_expanded = 0, 0, [], 0
    frontier = QQ.PriorityQueue()
    frontier.put((heuristics(initial_state),initial_state, 0, []))
    explored = set([])
    frontier_and_explored = set([])
    while not frontier.empty():
        state_set = frontier.get()
        state = state_set[1]
        explored.add(tuple(state))
        frontier_and_explored.add(tuple(state))
        parent_gn = state_set[2]
        action = state_set[3]
        if goalTest(state):
            return Success(state, max_fringe_size, parent_gn, frontier.qsize(), action, nodes_expanded, max_search_depth)
        nodes_expanded += 1
        index = state.index(0)
        # Neighbor list contains state as tuples
        # Action list contains all the actions affiliated with each neighbor
        neighbor_list, action_list = neighbors(index, state)

        for i in xrange(len(neighbor_list)):
            if neighbor_list[i] not in frontier_and_explored:
                frontier.put((heuristics(list(neighbor_list[i])) + 1 + parent_gn,list(neighbor_list[i]), parent_gn + 1, action + [action_list[i]]))
                frontier_and_explored.add(neighbor_list[i])
            else:
                avatar_h = heuristics(list(neighbor_list[i])) + 1 + parent_gn
                avatar = filter(lambda x: x[1] == neighbor_list[i] and x[2] < avatar_h,
                       frontier.queue)
                if avatar:
                    avantar_index = frontier.queue.index(avatar[0])
                    frontier.queue[avantar_index] = frontier.queue[avantar_index][:2] + (avatar_h, action + [action_list[i]])
                    break
            max_search_depth = max(max_search_depth, parent_gn + 1)
        max_fringe_size = max(max_fringe_size, frontier.qsize())

    return Failure()

class IDA(object):
    def loop_dfs(self, initial_state):
        bound = heuristics(initial_state)
        nodes_expanded = 0
        self.nodes_expanded = nodes_expanded
        count = 0
        # smallest = float("inf")
        while True:
            # if count == 2:
            #     break
            bound = self.DFS_inner(initial_state,bound, count)

            count += 1
        return

    def DFS_inner(self, initial_state, bound, count):
        max_fringe_size, max_search_depth, path_to_goal = 0, 0, []

        frontier = Stack()
        action = Stack()
        frontier.push((initial_state, 0))
        action.push(tuple([]))
        explored = {tuple(initial_state):heuristics(initial_state)}
        explored_frontier = {tuple(initial_state):heuristics(initial_state)}
        smallest = float("inf")
        while not frontier.isEmpty():

            state_set = frontier.pop()
            state = state_set[0]
            parent_gn = state_set[1]
            path_to_goal = action.pop()

            if goalTest(state):
                return Success(state, max_fringe_size, len(path_to_goal), frontier.size(), path_to_goal, self.nodes_expanded,
                               max_search_depth)

            index = state.index(0)
            self.nodes_expanded += 1

            neighbor_list, action_list = neighbors_reverse(index, state)
            for i in xrange(len(neighbor_list)):
                COST_CURRENT = parent_gn + 1 + heuristics(neighbor_list[i])
                if (neighbor_list[i] not in explored):
                    if COST_CURRENT <= bound:
                        explored[neighbor_list[i]] = COST_CURRENT
                        frontier.push((list(neighbor_list[i]), parent_gn + 1))
                        action.push(path_to_goal + (action_list[i],))
                        max_search_depth = max(max_search_depth, len(path_to_goal) + 1)
                    elif COST_CURRENT > bound:
                        smallest = min(smallest, COST_CURRENT)
                        # print smallest, "smallest"
                elif (explored[neighbor_list[i]] > COST_CURRENT):
                    explored[neighbor_list[i]] = COST_CURRENT
                    frontier.push((list(neighbor_list[i]), parent_gn + 1))
                    action.push(path_to_goal + (action_list[i],))
                    max_search_depth = max(max_search_depth, len(path_to_goal) + 1)
            max_fringe_size = max(max_fringe_size, frontier.size())
            # if count == 1:
            #     print bound
            #     print smallest, parent_gn
            #     print frontier.items
            #     print explored.items()

        # if smallest == float("inf"):
        #     smallest += 1
        return smallest

if __name__ == '__main__':
    start_time = time.clock()

    METHOD = sys.argv[1]
    INITIAL = sys.argv[2].split(',')
    # INITIAL = ['3','1','2','0','4','5','6','7','8']
    # METHOD = "ida"
    # INITIAL = [2, 1, 0, 6, 4, 5, 8, 3, 7]
    # INITIAL = ['1','2','5','3','4','0','6','7','8']
    # INITIAL = ['7','2','4','5','0','6','8','3','1']
    # INITIAL = ['0','8','7','6','5','4','3','2','1']
    # INITIAL = ['5','0','4','6','7','3','1','8','2']
    # INITIAL = [4,0,2,5,8,3,7,6,1]
    n = int(math.sqrt(len(INITIAL)))
    INITIAL = [int(i) for i in INITIAL]
    GOAL = sorted(INITIAL)
    if METHOD == "bfs":
        BFS_method(INITIAL)
    elif METHOD == "dfs":
        DFS_method(INITIAL)
    elif METHOD == "ast":
        AST_method(INITIAL)
    elif METHOD == "ida":
        ida = IDA()
        ida.loop_dfs(INITIAL)
    # BFS_method(INITIAL)
    # DFS_method(INITIAL)
    # AST_method(INITIAL)

    # print IDA_method(INITIAL)
    # method[METHOD]