tests
testFrozen
	"Test to check if block is not frozen when first created"
	
	b := Blocks new.
	b createBlock: '7' orientation: '1'.
	
	self assert: (b isFrozen) equals: false. 