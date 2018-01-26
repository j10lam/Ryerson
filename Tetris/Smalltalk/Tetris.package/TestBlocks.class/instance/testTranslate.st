tests
testTranslate
	"Test to see if the block shifted right 1 cell"
	
	| temp point1 point2 |
	
	b := Blocks new.
	b createBlock: '1' orientation: '1'.
	
	temp := (b getBlock) deepCopy.
	
	b translate: 1.
	
	1 to: (temp size) do: [:i |
		point1 := (b getBlock) at: i.
		point2 := (temp at: i).
		self assert: (point1 x) - (point2 x) equals: 1.
		]