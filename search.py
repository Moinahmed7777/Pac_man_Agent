# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
#from searchAgents import manhattanHeuristic

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    #[s, s, w, s, w, w, s, w]

    return  [s, s, w, s, w, w, s, w]

class Pac(object):

   

    def __init__(self, config, action="Initial", cost=0,parent=None):


        self.cost = cost
        

        self.parent = parent

        self.action = action

        self.config=config
        
        
        

'''
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
'''

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    from util import Stack
    
    s=Stack()
    f_dict={}
    start_state=Pac(problem.getStartState())
    
    s.push(start_state)
    Explored_set=set()
    
    
    while not s.isEmpty():
        curr_state=s.pop()
        
        
        f_dict[curr_state.config]=1
        Explored_set.add(curr_state.config)
        
        if problem.isGoalState(curr_state.config):
            
            return f_path(curr_state,start_state)
            
        
        
        for i in problem.getSuccessors(curr_state.config)[::-1]:
            if i[0] not in Explored_set and f_dict.get(i[0])==None:
                
                
                children=Pac(i[0],i[1],i[2],parent=curr_state)
                s.push(children)
        f_dict.pop(curr_state.config)
    
    
    
def f_path(curr_state,start_state):
    scon=start_state.config
    
    path=[]
    while not scon==curr_state.config:
        path.append(curr_state.action)
        curr_state=curr_state.parent
    path.reverse()
    return path
    


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    
    q=Queue()
    f_dict={}
    
    start_state=Pac(problem.getStartState())
    
    q.push(start_state)
    Explored_set=set()
    X=[]
    
    while not q.isEmpty():
        curr_state=q.pop()
        
        
        f_dict[curr_state.config]=1
        Explored_set.add(curr_state.config)
        
        if problem.isGoalState(curr_state.config):
            
            X=f_path(curr_state,start_state)
            
            break
        
        
        for i in problem.getSuccessors(curr_state.config):
            if i[0] not in Explored_set and f_dict.get(i[0])==None:
                
                #i.append(curr_state)
                children=Pac(i[0],i[1],i[2],parent=curr_state)
                q.push(children)
                f_dict[i[0]]=1
        
    return X
        
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    from util import PriorityQueue
    
    pq=PriorityQueue()
    f_dict={}
    start_state=Pac(problem.getStartState())
    
    pq.push(start_state,0)
    Explored_set=set()
    
    
    while not pq.isEmpty():
        curr_state=pq.pop()
        
        
        if problem.isGoalState(curr_state.config):

            return f_path(curr_state,start_state)
            
        Explored_set.add(curr_state.config)
        f_dict[curr_state.config]=curr_state.cost
        
        for i in problem.getSuccessors(curr_state.config):
            if i[0] not in Explored_set:
                
                cost=curr_state.cost+i[2]
                
                if f_dict.get(i[0])==None:
                
                    children=Pac(i[0],i[1],cost,parent=curr_state)
                    pq.push(children,cost)
                    f_dict[i[0]]=cost
                    
                elif cost<f_dict[i[0]]:
                    
                    children=Pac(i[0],i[1],cost,parent=curr_state)
                    pq.update(children,cost)
                    f_dict[i[0]]=cost
                    
        

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    
    pq=PriorityQueue()
    f_dict={}
    start_state=Pac(problem.getStartState())
    
    pq.push(start_state,0)
    Explored_set=set()
    
    while not pq.isEmpty():
        curr_state=pq.pop()
        
        if problem.isGoalState(curr_state.config):
            
            return f_path(curr_state,start_state)
            
        Explored_set.add(curr_state.config)
        f_dict[curr_state.config]=curr_state.cost
        
        
        for i in problem.getSuccessors(curr_state.config):
            #i = child nodes as tuple
            if i[0] not in Explored_set:
                
                g=curr_state.cost+i[2]
                
                #f(n)=g(n)+hueristic
                f=g+(heuristic( (i[0]), problem ))
                if f_dict.get(i[0])==None:
                
                    
                    children=Pac(i[0],i[1],g,parent=curr_state)
                    pq.push(children,f)
                    f_dict[i[0]]=g
                elif g<f_dict[i[0]]:
                    children=Pac(i[0],i[1],g,parent=curr_state)
                    pq.update(children,f)
                    f_dict[i[0]]=g
        


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
