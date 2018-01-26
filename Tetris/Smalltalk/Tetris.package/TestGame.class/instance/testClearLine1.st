tests
testClearLine1
	"Test to check if a filled line will be cleared once the current piece is frozen"

	| aLine |	
	g := Game new.
	g readFrom: 'board 5 10
dice 7 1 7 2
moves l+rrr+'.

	aLine := (g getBoard last: 2) first.
	
	self assert: aLine equals: '|     |'.

	