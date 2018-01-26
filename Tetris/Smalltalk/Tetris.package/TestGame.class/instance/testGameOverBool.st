tests
testGameOverBool
	"Test to see if the game has reached Game Over state - gameOver = true.
	 This means that no block is able to be spawned at the middle of the board.
	 There exists a block already there in the way."
	
	g:=Game new.
	g readFrom: 'board 4 5
dice 1 1
moves +++'.

	self assert: (g checkGameOver) equals: true.
	