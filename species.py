"""A class for each species in the game which contains the base population, speed, size, and power and possible mutations"""
from mutants import Mutants
from biome import Biome

class Species:
	
	def __init__(self, name):
		self.name = name
		self.population = 100
		self.mutants = []
		self.biomes = []

	def toString(self):
		return """Your name is {}. Population is {}""".format(self.name, 
			self.population)