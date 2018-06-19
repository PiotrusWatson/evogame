class Mutants:
	def __init__(self, name, species):
		self.name = name
		self.mutations = Mutations()
		self.species = species
		self.population = 1
		self.hunted_species = None
		self.SPECIES_THRESHOLD = 40
