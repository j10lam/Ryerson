tests
testSpawnOdd
	"Test to see if block spawns in the middle if given cols are odd"
	
	g:=Game new.
	g readFrom: 'board 5 4
dice 1 1
moves lr'.
	b := g getBoard.
	
	self assert: (b first = '| yy  |').
	
	