tests
testGameOverBoard
	"Test to check if Game Over state is reached. If so, no other block can be spawned onto the board.     If this test passes, then there should exist a blank line at the top of the board. This is
	 because one empty row is not succifient enough to spawn another block (i.e.: a square piece
	 requires two empty rows)"
	
	| aLine |
	
	g:=Game new.
	g readFrom: 'board 4 5
dice 1 1
moves +++'.
	aLine := (g getBoard) first: 2.

	self assert: (g checkGameOver) equals: true.
	self assert: (aLine first) equals: '|    |'.
	self assert: (aLine second) equals: '| yy |'.
	self assert: (g getNumPieces) equals: 2.