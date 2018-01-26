tests
testIfArrayExists
	"Test to see if the Array exists and is the same in the object"
	
	| anArray |
	
	anArray := #(1 2 3 4).
	d := Dice new.
	d setRoll: anArray.
	
	self assert: (d getSequence = anArray).