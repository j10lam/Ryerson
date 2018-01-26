tests
testLetter
	"Test to see if method returns the correct tetris piece"
	
	b := Blocks new.
	b createBlock: '7' orientation: '1'.
	
	self assert: (b getLetter) equals: $c. 