#!/usr/bin/python

from queue import Queue

# getSuccessors : string --> list
#
# returns all words with 1 letter offset either 1 up or 1 down
#
def getSuccessors(state, my_dict):
	successors = []
	for i in range(len(state)):

		# shift each char to any letter
		# 97 = ascii 'a'
		for k in range(0, 26):
			up = state[0:i] + chr(97 + k) + state[i+1:]
			
			if up in my_dict and up not in successors and up != state:
				successors.append(up)
	
	return successors


# goal : string --> boolean
#
# tests if current word is equal to goal word
#
def goal(word, goal_word):
	return (word == goal_word)


# makePath : String, dict --> list
#
# reverse engineers path to goal word using child --> parent dictionary
#
def makePath(state, p):
	path = [state]
	while(p[state] is not None):
		state = p[state]
		path.append(state)
	return path[::-1]



# transformWord : string, list --> list
#
# calculates the shortest path of words between start and goal words
#
def transformWord():
	
	# get required user input
	base_word = input("Enter base string: ")
	goal_word = input("Enter goal string: ")
	dict_path = input("Enter path to dictionary: ")

	# read in dict
	my_dict = {}
	for line in  open(dict_path, 'r'):
		my_dict[line.strip().lower()] = 1

	# initialize queue
	q = Queue()
	q.put(base_word)

	# initialize parents / path dict
	p = { base_word:None }

	# try to transform base word into goal word
	while(not q.empty()):

		# pop off head of queue
		state = q.get()

		# if goal; return
		if goal(state, goal_word):
			return makePath(state, p)

		# else store new successors in dict and queue
		successors = getSuccessors(state, my_dict)
		for s in successors:
			if (s not in p):
				p[s] = state
				q.put(s)


# run program
path = transformWord()
if path:
	for node in path:
		print(node)

else:
	print("Could not find a path")