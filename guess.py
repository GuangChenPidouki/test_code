class GuessNumber:
	def __init__(self, max):
		self.max = max
		self.guess_num = -1
		self.guess_times = 0
		self.game_times = 0
		self.avg = 0

	def main_loop(self):
		while(True):
			while(self.game_times != 0):
				decide = input("Play again?")
				if(decide in ['y', 'n']):
					break
				else:
					print("Please input 'y'--[yes] or 'n'--[no]")
			if((self.game_times == 0) or decide == 'y'):
				self.start_guess()
			else:
				return

	def start_guess(self):
		low = 1
		high = self.max
		while(low <= high):
			if(low == high):
				self.guess_num = low
				self.finish_print()
				return
			n = self.guess(low, high)
			while(True):
				decide = input("%d ?" % n)
				if(decide not in ['h', 'l', 'c']):
					print("Please input 'l'--[low] or 'h'--[high] or 'c'--[correct]")
				elif(((n == low) and (decide == 'h')) or ((n == high) and (decide == 'l'))):
					print("As guessed number already touch limit %d, you cannot go beyond" % n)
				else:
					break
			if(decide == 'h'):
				high = n - 1
				self.guess_times += 1
			elif(decide == 'l'):
				low = n + 1
				self.guess_times += 1
			else:
				self.guess_times += 1
				self.guess_num = n
				self.finish_print()
				return
			assert(low <= high)

	def guess(self, low, high):
		return (low + high) // 2

	def finish_print(self):
		print("Your number is %d." % self.guess_num)
		print("It took me %d guesses." % self.guess_times)
		total = self.game_times * self.avg + self.guess_times
		self.game_times += 1
		self.avg = total/float(self.game_times)
		print("I averaged %f guesses per game for %d game(s)." % (self.avg, self.game_times))
		self.guess_times = 0

def main():
	while(True):
		try:
			n = int(input("Please enter a number n: "))
			if(n <= 0):
				print("Input should be a valid positive number")
			else:
				break
		except ValueError:
			print("That was no valid number.  Try again...")
	game = GuessNumber(n)
	game.main_loop()

if __name__ == "__main__":
	main()
