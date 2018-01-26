tests
testDown
	"Test to see if the block shifted down 1 cell"
	
	| temp point1 point2 |
	
	b := Blocks new.
	b createBlock: '1' orientation: '1'.
	
	temp := (b getBlock) deepCopy.
	
	b down: 1.
	
	1 to: (temp size) do: [:i |
		point1 := (b getBlock) at: i.
		point2 := (temp at: i).
		self assert: (point1 y) - (point2 y) equals: 1.
		]