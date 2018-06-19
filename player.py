import uuid

class Player: 

	def __init__(self, name):
		self.name = name
		self.mutant_list = []
		self.player_ID = uuid.uuid4()
