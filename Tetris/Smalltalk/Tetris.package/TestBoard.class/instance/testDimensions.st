tests
testDimensions
	"Test to see if board dimensions are equal to the given parameters at instantiation"
	
	| anArray |
	
	anArray := #('2' '3').
	b := Board new.
	b createBoard: anArray.
	
	self assert: (anArray first asInteger) equals: (b getDimension x).

