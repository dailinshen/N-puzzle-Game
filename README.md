# N-puzzle-Game
## AI Search Agent Task


1. Implementation  
Implement the following four algorithms as demonstrated in lecture. In particular:  

• Breadth-First Search. Use an explicit queue, as shown in lecture.  
• Depth-First Search. Use an explicit stack, as shown in lecture.    
• A-Star Search. Use a priority queue, as shown in lecture. For the choice of heuristic, use the Manhattan priority function; that is, the sum of the distances of the tiles from their goal positions. Note that the blanks space is not considered an actual tile here.  
• IDA-Star Search. As before, for the choice of heuristic, use the Manhattan priority function. Recall from lecture that implementing the Iterative Deepening Search (IDS) algorithm involves first implementing the Depth-Limited Search (DLS) algorithm as a subroutine. Similarly, implementing the IDA-Star Search algorithm involves first implementing a modified version of the DLS algorithm that uses the heuristic function in addition to node depth.  

2. Order of Visits  
In this implementation, we always visit child nodes in the "UDLR" order; that is, [‘Up’, ‘Down’, ‘Left’, ‘Right’] in that exact order. Specifically:  
  
• Breadth-First Search. Enqueue in UDLR order; dequeuing results in UDLR order.  
• Depth-First Search. Push onto the stack in reverse-UDLR order; popping off results in UDLR order.    
• A-Star Search. Since you are using a priority queue, what happens when there are duplicate keys? What do you need to do to ensure that nodes are retrieved from the priority queue in the desired order?  
• IDA-Star Search. For each iteration, you can handle node ordering as you would in depth-first search.  
