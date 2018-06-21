from species import Species
from player import Player

class GameState:

#game start
	def __init__(self):
		self.species_list = [Species("Blob")] 
		self.biome_list = [] #todo: make a graph
		self.id_to_player = {}

		
		#placeholder, set up empty player
		self.add_player(Player("placeholder"))


	def add_player(self, new_player):
		self.id_to_player[new_player.player_ID] = new_player 

	def get_player(self, player_id):
		return self.id_to_player.get(player_id, None)

	#placeholder function, todo remove
	def get_arbitrary_player(self):
		return next(iter(self.id_to_player.values()))

	def list_players(self):
		for player_id, player in id_to_player.iteritems():
			print(player_id, player.name)



