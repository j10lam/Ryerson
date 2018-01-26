tests
testRotateLeft
	"Test to see if the block rotated left"
	| cells temp |
	
	b := Blocks new.
	b createBlock: '6' orientation: '4'.
	cells := b getBlock.
	
	temp := OrderedCollection with: 0@0 with: (-1)@0 with: 0@1 with: 0@(-1).

	cells do: [:pt |
		self assert: (temp includes: pt)].
	
	
	
	
	
	
	
	