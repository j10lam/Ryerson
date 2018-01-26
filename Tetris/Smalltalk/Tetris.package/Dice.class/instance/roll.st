action
roll
	"roll increments i and returns the item at sequence[i]"
	
	i := i + 1.
		
	(i > sequence size) ifTrue: [ 
		i := 1
		].
		
	^(sequence at: i).
	