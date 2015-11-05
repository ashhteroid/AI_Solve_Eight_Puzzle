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

if __name__=="__main__":
	#algo(init_state,strategy)
	print "Eight Puzzle Type Puzzle Solver"
	size=int(math.sqrt(int(raw_input("What Puzzle to solve(Example: '8' for Eight puzzle or '15' for fifteen puzzle) \n"))+1))
	print "Please enter your puzzle as a sequence of comma seperated rows(Example: 1,2,3). Use a zero to represent the blank"
	init_state=[]    
	for i in xrange(size):
		init_state.append([int(x) for x in raw_input().split(',')])	
	print "Please enter desired goal state as a sequence of comma seperated rows(Example: 1,2,3). Use a zero to represent the blank"
	goal_state=[]
	for i in xrange(size):
		goal_state.append([int(x) for x in raw_input().split(',')])	
	
