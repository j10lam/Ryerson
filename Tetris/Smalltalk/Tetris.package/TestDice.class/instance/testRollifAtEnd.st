tests
testRollifAtEnd
	"Test to see if roll will iterate over the list from the beginning once it reaches the end"
	
	| anArray item  |
	
	anArray := #(1 2 3 4).
	d := Dice new.
	d setRoll: anArray.
	
	4 timesRepeat: [ d roll ].
	
	self assert: (d roll = 1).