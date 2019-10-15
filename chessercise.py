import sys
import re

def list_move(x, y, chess_type):
	base_dir = [(1,0), (0,1), (-1,0), (0,-1)]
	dia_dir = [(1,1), (1,-1), (-1,1), (-1,-1)]
	kni_dir = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
	if(chess_type.lower() == 'queen'):
		yield from move(x, y, base_dir + dia_dir, 8)
	elif(chess_type.lower() == 'knight'):
		yield from move(x, y, kni_dir, 1)
	elif(chess_type.lower() == 'rook'):
		yield from move(x, y, base_dir, 8)
	elif(chess_type.lower() == 'bishop'):
		yield from move(x, y, dia_dir, 8)
	elif(chess_type.lower() == 'king'):
		yield from move(x, y, base_dir + dia_dir, 1)
	else:
		print("No such chess type defined")

def move(orig_x, orig_y, directions, max_step):
	for dir_x, dir_y in directions:
		x, y = orig_x, orig_y
		step = max_step
		while(step > 0):
			x += dir_x
			y += dir_y
			if(isValid(x, y)):
				yield to_chess(x, y)
			else:
				break
			step -= 1

def isValid(x, y):
	if(x < 0 or x > 7 or y < 0 or y > 7):
		return False
	return True

def to_chess(x, y):
	return chr(ord('a')+x) + str(y+1)

def from_chess(pos):
	pattern = re.compile("^[a-z][0-9]$")
	if(len(pos) != 2 or not pattern.match(pos)):
		return (-1, -1)
	return (ord(pos[0])-ord('a'), int(pos[1])-1)

def usage():
	print("chessercise.py -piece KNIGHT -position d2")

def main():
	if((len(sys.argv) != 5) or (sys.argv[1] != "-piece") or (sys.argv[3] != "-position")):
		usage()
		return

	chess_type = sys.argv[2]
	position = sys.argv[4]

	x, y = from_chess(position)
	if(not isValid(x,y)):
		print("Not valid staring position")
		return
	for pos in list_move(x, y, chess_type):
		print(pos, end = ',')
	sys.stdout.write("\b \n")

if __name__ == "__main__":
	main()
