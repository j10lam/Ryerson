initialization
startGame
	"startGame begins the Tetris game until all moves commands are consumed"
	
	dice ifNotNil: [  
		self setUpBlock.
	].
	
	moveList do:[:moves |
		moves do:[:move |
				
			(block isFrozen) ifFalse: [ 
				 self moves: (move asString)
				].
			
			(block isFrozen) ifTrue: [
				self addToBoard.
			   board clearLine: true.
				
				prevBlock := block deepCopy.
				self setUpBlock.
				
				gameOver ifTrue: [
					numPieces := numPieces - 1. 
					^self ].
				 ].
			].
		].
	
	block ifNotNil: [
		(block isFrozen) ifFalse: [
			self addToBoard ].
		].