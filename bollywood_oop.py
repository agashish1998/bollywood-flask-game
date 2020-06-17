
from movie_list import movies
import random

max_trials = 9
starter = ['A', 'E', 'I', 'O', 'U']


class bollywood:
	
	def __init__(self):
		self.movie_name = random.choice(movies).upper()
		self.player_name = ""
		self.trials = 9
		self.wrong_guessed_letters = starter
		self.guessed_letters = starter
		self.pre_movie = ""
		
	def check_guess(self, x):
		for a in self.movie_name:
			if a == x:
				return True
		return False
		
	def print_movie(self):
		s = ""
#		print(self.guessed_letters)
		for a in self.movie_name:
			if a == ' ':
				s += ' '
			elif a in self.guessed_letters:
				s += a
			else:
				s += '_'
		return s.split()
		
	def check_final_solution(self):
		for a in self.movie_name:
			if a not in self.guessed_letters and a != ' ':
				return False
		return True
		
	def print_bollywood(self):
		s = 'BOLLYWOOD'
		x = ''
		for i in range(self.trials):
			x += s[i]
		for i in range(self.trials, 9):
			x += '_'
		return x
		
	def reset(self):
#		print("resetting the game")
		self.trials = max_trials
		self.guessed_letters = ['A', 'E', 'I', 'O', 'U']
		self.wrong_guessed_letters = ['A', 'E', 'I', 'O', 'U']	
		self.pre_movie = self.movie_name
		self.movie_name = random.choice(movies).upper()
#		print(self.guessed_letters, self.wrong_guessed_letters)
		
		
	def input_handle(self, g):
			
		g = g.upper()
		
		for a in g:
			if(a < 'A' or a >'Z' or (a in self.guessed_letters) or (a in self.wrong_guessed_letters)):
				continue
			if self.check_guess(a):
				self.guessed_letters.append(a)
			else:
				self.trials = self.trials -1
				self.wrong_guessed_letters.append(a)
                
                
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
			
	
