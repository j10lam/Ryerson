Class: 
I represent the blocks of the Tetris game

Responsibility: 
I instantiate and hold a collection of various  block types.
I manipulate each block through rotation, translation, etc.
I hold 3 states for each block (initial, current, previous).

Collaborators:
I collaborate with the Game - the game handles all aspects of the Blocks class 
I collrborate with the Dice - dice dictates which block type is created
I collaborate with the Board - I do calculations based on the board cells.

Instantiation Example:
b := Blocks new.
b createBlock: (anInteger  asString) orientation: (anInteger asString)
 
Internal Representation and Key Implementation Points.

    Instance Variables
	current:		<Object>
	frozen:		<Object>
	initial:		<Object>
	letter:		<Object>
	previous:		<Object>