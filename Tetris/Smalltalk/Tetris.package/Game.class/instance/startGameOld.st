initialization
startGameOld
	"startGame begins the Tetris game until all moves commands are consumed"

	moveList do:[:moves |
		moves do:[:move |
			
			(block isNil) ifTrue: [
				block := Blocks new.
				block createBlock: (dice roll) orientation: (dice roll).
				self spawnBlock.
				
				gameOver ifTrue: [ 
					^self ].
				
				numPieces := numPieces + 1.
				].
			
			(block isFrozen) ifFalse: [ 
				 self moves: (move asString)
				].
			
			(block isFrozen) ifTrue: [
				self addToBoard.
				block := nil.
				board clearLine: true.
				 ].
			].
		].
	
	block ifNotNil: [	
		(block isFrozen) ifFalse: [
		self addToBoard ].
	].