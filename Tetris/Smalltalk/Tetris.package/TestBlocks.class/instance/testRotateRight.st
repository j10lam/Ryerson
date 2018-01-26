tests
testRotateRight
	"Test to see if the block rotated right"
	| cells temp |
	
	b := Blocks new.
	b createBlock: '6' orientation: '2'.
	cells := b getBlock.
	
	temp := OrderedCollection with: 0@0 with: 0@1 with: 1@0 with: 0@(-1).

	cells do: [:pt |
		self assert: (temp includes: pt)].
	
	
	
	
	
	
	
	