'''  ==========================================================================
  @version  1.0
  @author   Ashwin Ramadevanahalli
  @title    Solving Eight Puzzle using A Star and Uniform cost Search.
 	 =========================================================================='''
'''
Example
goal_state=[[1,2,3]
			[4,5,6]
			[7,8,0]]

init_state=[[1,8,2]
			[0,4,3]
			[7,6,5]]

def algo:
	queue=init_state
	while(queue not empty)
		minnode=queue.pop(min(queue))
		if minnode==goal_state
			print "Solution found"
			return minnode
		else 
			queue.append(childrn of minnode)
	print "Failure: No Solution"	
'''
import math 



def swap(state,i,j,k,l):
	newstate=[]
	for m in xrange(size):
		newstate[m]=state[m][:]
	newstate[i-1][j-1]=state[k-1][l-1]
	newstate[k-1][l-1]=state[i-1][j-1]
	return newstate

# All possible next moves from the current state
def possible_next_moves(state):
    possible_states = []
    i=0
    j=0
    for row in input_list:
    	i=i+1
    	for col in row:
    		j=j+1
    		if col==0:
				break
		break
	if i<size 
		possible_states.append(swap(state,i,j,i+1,j))
	if j<size
		possible_states.append(swap(state,i,j,i,j+1))
	if i>1
		possible_states.append(swap(state,i,j,i-1,j))
	if j>1
		possible_states.append(swap(state,i,j,i,j+1))
	return possible_states

def distance(i,j,elem,goal):
    for m in range(len(goal)):
        for n in range(len(goal[i])):
            if (elem == goal[m][n]):
                return int(math.fabs(n-i) + math.fabs(n-j))
            
#Manhattan distance from current state and goal state
def manhattan_distance(state,goal):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            try:
                int(state[i][j])
                distance = (distance + 
                    distance(i,j,state[i][j],goal))
            except:
                pass
    return distance

def 


def algo(init,goal):
	
	OPEN.append(init)

	while(True):
        if (len(OPEN)==0):
            print "No solution"
            return

        lowindex = 0
        low = OPEN[0]['f']
        for i in range(len(OPEN)):
            number = OPEN[i]['f']
            if (number<low):
                lowindex = i
                low = number
        n = OPEN[lowindex] # n is current state
        """
        # code block to print states explored
        for i in range(len(n['state'])):
            print ''.join(n['state'][i])
        print n
        """
        OPEN.pop(lowindex)
        
        if (n['state']==goal):      #print path to goal when goal is found
            temptrav = n
            path_to_goal = []
            while (temptrav!=None):
                path_to_goal.append(temptrav)
                temptrav = temptrav['ancestor']
            while (len(path_to_goal)!=0):
                pathnode =  path_to_goal.pop()
                for i in range(len(pathnode['state'])):
                    print ''.join(pathnode['state'][i])
                print "\n"
            print "this is goal"
            return

        m = []                  #list of next possible moves
        m = possible_next_moves(n['state'])
        M = []                  #calculate heuristic function for possible moves
        for i in range(len(m)):
            tempdict =  {
                'state': m[i],
                'f': 0,
                'g': n['g']+1,
                'h': manhattan_distance(m[i],goal),
                'ancestor': n
            }
            tempdict['f'] = tempdict['g'] + tempdict['h']
            M.append(tempdict)

        for i in range(len(M)):
            if (CLOSED.count(M[i])==0):
                OPEN.append(M[i])
        CLOSED.append(n)





if __name__=="__main__":
	#algo(init_state,strategy)
	print "Eight Puzzle Type Puzzle Solver"
	global size=int(math.sqrt(int(raw_input("What Puzzle to solve(Example: '8' for Eight puzzle or '15' for fifteen puzzle) \n"))+1))
	print "Please enter your puzzle as a sequence of comma seperated rows(Example: 1,2,3). Use a zero to represent the blank"
	init_state=[]    
	for i in xrange(size):
		init_state.append([int(x) for x in raw_input().split(',')])	
	print "Please enter desired goal state as a sequence of comma seperated rows(Example: 1,2,3). Use a zero to represent the blank"
	goal_state=[]
	for i in xrange(size):
		goal_state.append([int(x) for x in raw_input().split(',')])

	init=  {
    'state': init_state,
    'f': manhattan_distance(init_state,goal_state),
    'g': 0,
    'h': manhattan_distance(init_state,goal_state),
    'Parent': None
			}	

	global OPEN
	global CLOSED
	algo(init,goal)



