tests
testPowerupClearLine
	"Test to check if ONLY the bottom most line with only one empty cell will be cleared when a powerup is triggered"

	| aLine |	
	g := Game new.
	g readFrom: 'board 5 10
dice 7 1 7 1 1 1
powerup 1 9.
moves l+l+l'.

	aLine := (g getBoard last: 3).
	
	self assert: (aLine first)  equals: '|cccc |'.
	self assert: (aLine second) equals: '|     |'.


	