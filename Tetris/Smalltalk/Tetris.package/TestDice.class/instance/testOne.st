tests
testOne
	"Mason Dice Test1"
	
	| dice |
	
	self assert: dice equals: nil. 
	dice := Dice new.
	#((1 2 3 4) (7 2 9 3)) do: [: seq |
		dice setRoll: seq.
		2 timesRepeat: [
			seq do: [: each |
				self assert: (dice roll) equals: each
	]]].