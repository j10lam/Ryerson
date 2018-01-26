tests
testSquareRotation
 	"Test to check if square can be rotated.
	 If assertion passes - move is consumed but square is not rotated."

	g:=Game new.
	g readFrom: 'board 4 5
dice 1 1
moves R'.
	b := g getBoard.
	
	self assert: (b first) equals: '| yy |'.
	self assert: (b second) equals: '| yy |'.
	