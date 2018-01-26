action
rotate: direction
	"rotate: direction - rotates all items in the OrderedCollection, initial, left or right.
	 It then calls the method teleport to change the values in the collection, current."

	| temp |
	
	(letter = $y) ifTrue: [ 
		^self].

	initial do:[:item | 
		temp := item.
		
		(temp = (initial first)) ifFalse: [ 
			(direction = 'L') ifTrue: [ 
				temp := temp leftRotated.].
			(direction = 'R') ifTrue: [ 
				temp := temp rightRotated.].
			].	
			
		item setX: temp x setY: temp y.
		].
	
	self teleport.