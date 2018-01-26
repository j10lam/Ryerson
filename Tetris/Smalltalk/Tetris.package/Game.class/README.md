Class:
I repesent the Tetris game.

Responsibilities:
I  am responsible for instantiating all objects in other classes (i.e.: Blocks, Board, Dice)
I am responsible for running the game and manipulating each block on the board
I am responsible for checking constraints (i.e.: bounds, collisions)
I am responsible for reading and writing to and from ReadStreams/WriteStreams.

Collaborators:
Blocks  - I instantiate all block objects  and handle their movements
Board - I instantiate the board and tells it when to clearLines
Dice - I instantiate the dice and request for a roll when needed.

Instantiation Example:
g := Game new.
g readFrom: (aString or ReadStream))
 
Internal Representation and Key Implementation Points.

    Instance Variables
	block:		<Object>
	board:		<Object>
	bottom:		<Object>
	commands:		<Object>
	dice:		<Object>
	hit:		<Object>
	moveList:		<Object>
	powerups:		<Object>