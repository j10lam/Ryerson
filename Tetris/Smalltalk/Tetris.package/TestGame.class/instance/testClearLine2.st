tests
testClearLine2
	"Test to check if multiple filled lines will be cleared once the current piece is frozen"

	| aLine |	
	g := Game new.
	g readFrom: 'board 6 10
dice 7 1 7 1 1 1
moves l+l+rr+'.

	aLine := (g getBoard last: 3).
	
	self assert: (aLine first) equals: '|      |'.
	self assert: (aLine second) equals: '|      |'.

	