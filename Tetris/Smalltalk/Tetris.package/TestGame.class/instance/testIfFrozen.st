tests
testIfFrozen
	"Test to see if block becomes frozen once it reaches the bottom"
	
	g:=Game new.
	g readFrom: 'board 4 4
dice 1 1
moves ..'.
	b := g getBlock.
	self assert: (g getPrevBlock isFrozen).