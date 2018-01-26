action
clearLine: aFullLine
	"clearLine: aFullLine - finds either completely filled lines 
	 or lines containing only one empty cell (depends on the bool - aFullLine).
	
	 Ex.:
	 if (aFullLine) --> search for filled lines
	 else --> search for lines with only one cell missing
	
	 Removes all lines that fit such criteria. Note: if (aFullLine = False) removes only the last          occurence that meets the criteria."

	| temp line |
	temp := OrderedCollection new.
	
	1 to: rows do: [ :i |
		line := template at: i.
		
		aFullLine ifTrue: [
			(line includes: $ ) ifFalse: [ 
				temp add: i. 
				]
			 ].
		
		aFullLine ifFalse: [
			((line occurrencesOf: $ ) = 1) ifTrue: [ 
				temp removeAll.
				temp add: i.  
				 ]
			 ].
	].
	
	temp do: [ :l |
		template at: l put: emptyRow. ]
	