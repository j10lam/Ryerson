Class:
 I represent the dice for the Tetris game.

Responsibility: 
I dictate which piece or  orientation the next block will be.

Collaborator:
I collaborate with the Game class.
When called, I roll the the dice (anArray of Integers) and return an element inside the given array.

Instantiation Example:
d := Dice new.
d createDice: (anArray of Strings)

Internal Representation and Key Implementation Points.

    Instance Variables
	i:		<Object>
	j:		<Object>
	piece:		<Object>
	pos:		<Object>
	sequence:		<Object>