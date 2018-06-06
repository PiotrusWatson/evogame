"""A class for each species in the game which contains the base population, speed, size, and power and possible mutations"""
from mutations import Mutations 

class Species:
	
	def __init__(self, name):
		self.name = name
		self.population = 100
		self.speed = 1.0
		self.size = 1.0
		self.power = 1.0
		self.mutations = Mutations()

	def toString(self):
		return """Your name is {}. Population is {}, Speed is {}, 
		Size is {}, Power is {}""".format(self.name, self.population, 
			self.speed, 
			self.size, 
			self.power)