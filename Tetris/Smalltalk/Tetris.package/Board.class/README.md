Class:
I represent the Board of the Tetris game

Responsibility:
I instantiate the board of the Tetris game.
I clear any full or partially filled lines off the board
I send information to the receiver.

Collaborators:
I collaborate with the Game class. it adds items onto the board  and requests to remove lines from the board.

Instantiation Example:
b := Board new.
b createBoard: (anArray of Integers asString)
 
Internal Representation and Key Implementation Points.

    Instance Variables
	cols:		<Object>
	emptyRow:		<Object>
	rows:		<Object>
	template:		<Object>