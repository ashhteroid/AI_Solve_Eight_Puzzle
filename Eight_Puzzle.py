/*  =============================================================================
  @version  1.0
  @author   Ashwin Ramadevanahalli
  @title    Solving Eight Puzzle using A Star and Uniform cost Search.
  ========================================================================== */

goal_state=[[1,2,3]
			[4,5,6]
			[7,8,0]]

init_state=[[1,8,2]
			[0,4,3]
			[7,6,5]]




def algo:
	queue=init_statea
	while(queue not empty)
		minnode=queue.pop(min(queue))
		if minnode==goal_state
			print "Solution found"
			return minnode
		else 
			queue.append(childrn of minnode)
	print "Failure: No Solution"	

if __name__=="__main__":
	algo(init_state,strategy)

