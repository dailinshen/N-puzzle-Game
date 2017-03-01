# N-puzzle-Game
## AI Search Agent Task

#### INSTRUCTIONS ####   
This project creates an agent to solve the n-puzzle game (i.e. the 8-puzzle game generalized to an n × n array).   

**1 Introduction**  
An instance of the n-puzzle game consists of a board holding n^2 − 1 distinct movable tiles, plus an empty space. The tiles are numbers from the set {1, ..., n^2 − 1}. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this project, we will represent the blank space with the number 0.  
Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order ⟨0, 1, ..., n^2 − 1⟩. The search space is the set of all possible states reachable from the initial state.  
The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time. The cost of moving from one configuration of the board to another is the same and equal to one. Thus, the total cost of path is equal to the number of moves made from the initial state to the goal state.  

**2 Algorithm Review**   
Searches begin by visiting the root node of the search tree, given by the initial state. Among other book-keeping details, three major things happen in sequence in order to visit a node:  
• First, we remove a node from the frontier set.  
• Second, we check the state against the goal to determine if a solution has been found.  
• Finally, if the result of the check is negative, we then expand the node. To expand a given node, we generate successor nodes adjacent to the current node, and add them to the frontier set. Note that if these successor nodes are already in the frontier, or have already been visited, then they should not be added to the frontier again.  

This describes the life-cycle of a visit, and is the basic order of operations for search agents in this assignment—(1) remove, (2) check, and (3) expand. In this project, we will implement algorithms as described here.

**3 Implementation**  
Implement the following four algorithms as demonstrated in lecture. In particular:  
• Breadth-First Search. Use an explicit queue, as shown in lecture.  
• Depth-First Search. Use an explicit stack, as shown in lecture.    
• A-Star Search. Use a priority queue, as shown in lecture. For the choice of heuristic, use the Manhattan priority function; that is, the sum of the distances of the tiles from their goal positions. Note that the blanks space is not considered an actual tile here.  
• IDA-Star Search. As before, for the choice of heuristic, use the Manhattan priority function. Recall from lecture that implementing the Iterative Deepening Search (IDS) algorithm involves first implementing the Depth-Limited Search (DLS) algorithm as a subroutine. Similarly, implementing the IDA-Star Search algorithm involves first implementing a modified version of the DLS algorithm that uses the heuristic function in addition to node depth.  

**4 Order of Visits**  
In this implementation, we always visit child nodes in the "UDLR" order; that is, [‘Up’, ‘Down’, ‘Left’, ‘Right’] in that exact order. Specifically:  
• Breadth-First Search. Enqueue in UDLR order; dequeuing results in UDLR order.  
• Depth-First Search. Push onto the stack in reverse-UDLR order; popping off results in UDLR order.    
• A-Star Search. Since you are using a priority queue, what happens when there are duplicate keys? What do you need to do to ensure that nodes are retrieved from the priority queue in the desired order?  
• IDA-Star Search. For each iteration, you can handle node ordering as you would in depth-first search.  
