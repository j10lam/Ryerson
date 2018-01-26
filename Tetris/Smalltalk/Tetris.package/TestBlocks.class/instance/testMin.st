tests
testMin
	"Test to see if method returns correct minimum y value in a collection of points"
	
	b := Blocks new.
	b createBlock: '1' orientation: '1'.
	
	self assert: (b findMin) equals: -1. 