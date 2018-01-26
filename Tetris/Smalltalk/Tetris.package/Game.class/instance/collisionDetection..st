action
collisionDetection: fall
	"collisionDetection: fall - checks to see if there any non-empty cells on the board where
	 the current tetris piece will move onto after a move command is received."

	| piece temp count cell|

	count := 0.
	hit := false.
	piece := block getBlock.
	
	piece do:[:pt |
		(pt y = -1) ifTrue: [
			hit := true.
			^self.]
		].
	
	piece do:[:pt |
		cell := (pt x + 2)@(pt y + 1).
		temp := ((board getBoard) at: (cell y)) at: (cell x).
		(temp = $x) ifTrue: [ 		
			count := count + 1
			].		
		(temp = $ ) | (temp = $x) ifFalse: [
			hit := true.
				].
		].
	
	(fall) ifFalse: [
		count timesRepeat: [ 
			board clearLine: false.
			].
		]