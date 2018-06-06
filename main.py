from species import Species

#Placeholder
def show_map(void):
	print("showin map")
#placeholder
def move(direction):
	if (direction == None):
		print("please enter a direction")
	else:
		print("movin in", direction)

def list_species(void):
	print("listing all species on current biome")

def end_turn(void):
	print ("ending turn")

def mutate(mutation):
	if (mutation == None):
		print("listing available mutations")
	else:
		print("mutating to", mutation)

def list_mutations(available):
	if (available == None):
		print("showing current mutations")
	else:
		print("showing all mutations")

def my_species(void):
	print(fox.toString())

def error(void):
	print("I do not understand. Commands are: ")
	for command in command_to_function:
		print(command)



command_to_function = {"map": show_map, 
"move": move,
"species": list_species, 
"end_turn": end_turn, 
"mutate": mutate,
"mutations": list_mutations,
"my_species": my_species,
}

def main():
	init()
	print("Welcome to evogame! What do you want to do?")
	while (True):
	    entered_text = input("Enter a command: ")
	    if (" " in entered_text):
	    	command, argument = entered_text.split(" ")
	    	
	    else:
	    	command = entered_text
	    	argument = None

	    command_to_function.get(command, error)(argument)
	    
def init():
	global fox
	fox = Species("Fox")









if __name__ == '__main__':
	main()