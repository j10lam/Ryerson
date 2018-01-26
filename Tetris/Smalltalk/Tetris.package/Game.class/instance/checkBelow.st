action
checkBelow
	"checkBelow checks to see if there any non-empty cells under the current tetris piece.
	 If there is something below, the block's instance variable is set to frozen.
	 This block can no longer move."

	| piece temp |
	
	piece := block getBlock.
	bottom := 0.
	
	
	piece do:[:pt |
		(pt y > bottom) ifTrue: [ 
			bottom := pt y].
		].
		
	piece do:[:pt |
		temp := ((board getBoard) at: (bottom + 2)) at: (pt x + 2).
		(temp = $ ) | (temp = $x) ifFalse: [
			block setFrozen].
		].
	