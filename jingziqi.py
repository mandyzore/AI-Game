import random


STATES_MATRIX = [
	[None, None, None],
	[None, None, None],
	[None, None, None],
]

ROLES = {
	1: "Black",
	0: "White"
}

winer = None

def move(states_matrix, role):

	game_state = detect_end(states_matrix)

	if game_state=="win":
		winer = ROLES[abs(role-1)]
		print("{} win and {} fail".format(ROLES[abs(role-1)], ROLES[role]))
		return "win" # .format(ROLES[abs(role-1)], ROLES[role]))
	elif game_state=="full":
		return "draw"
	elif game_state=="continue":
		pass
		print("{} is taking move...".format(ROLES[role]))

	candidate_moves = detect_candidate_move(states_matrix)
	next_move = candidate_moves[random.choice(range(len(candidate_moves)))]
	(x, y) = next_move
	states_matrix[x][y] = role # 0 or 1
	
	return states_matrix

def detect_candidate_move(states_matrix):
	candidate_moves = []
	for x in range(len(states_matrix)):
		for y in range(len(states_matrix[x])):
			position_index = (x, y)
			if states_matrix[x][y]==None:
				candidate_moves.append(position_index)

	return candidate_moves

	

def detect_end(states_matrix):
	if detect_win(states_matrix):
		return "win"
	elif detect_full(states_matrix):
		return "full"
	else:
		return "continue"

def detect_full(states_matrix):
	full = True
	for row in states_matrix:
		for cell in row:
			if cell==None:
				full = False
				break
	return full

def detect_win(states_matrix):
	rows = states_matrix
	cols = [ [ states_matrix[row][col] for row in range(len(states_matrix))] for col in range(len(states_matrix)) ]
	duijiaoxian = [ [states_matrix[i][i] for i in range(len(states_matrix))], [states_matrix[len(states_matrix) - (i+1)][i] for i in range(len(states_matrix))]]
	
	for row in rows:
		win = True
		role = row[0]
		for cell in row:
			if cell!=role or cell==None:
				win = False
		if win==True:
			return win

	for row in cols:
		win = True
		role = row[0]
		for cell in row:
			if cell!=role or cell==None:
				win = False
		if win==True:
			return win

	for row in duijiaoxian:
		win = True
		role = row[0]
		for cell in row:
			if cell!=role or cell==None:
				win = False
		if win==True:
			return win

	return win


def self_play():
	states_matrix = [
		[None, None, None, None, None],
		[None, None, None, None, None],
		[None, None, None, None, None],
		[None, None, None, None, None],
		[None, None, None, None, None],

	]
	
	result = states_matrix
	while(detect_end(states_matrix)=="continue"):
		print(detect_end(states_matrix))
		# print_matrix(states_matrix)
		result = move(states_matrix, 1)
		print_matrix(states_matrix)

		if result!="win" or result!="draw":
			states_matrix = result
			move(states_matrix, 0)
			print_matrix(states_matrix)
		else:
			print_matrix(states_matrix)
			break
		
	print("DONE: {}".format(detect_end(states_matrix)))
	# print_matrix(states_matrix)

def print_matrix(states_matrix):
	out = ""
	for row in states_matrix:
		out_row = [ (str(i) if i!=None else "-") for i in row]
		line = " ".join(out_row) + "\n"
		out+=line
	print(out)
	return out 


if __name__ == '__main__':
	print("start...")
	self_play()







