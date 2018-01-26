tests
testLineRotation
 	"Test to check if line can be rotated if the first move command is rotate.
	 If assertion passes - means line cannot rotate if spawned on first row"

	g:=Game new.
	g readFrom: 'board 5 5
dice 7 1
moves R'.
	b := g getBoard.
	
	self assert: (b first) equals: '|cccc |'.
	