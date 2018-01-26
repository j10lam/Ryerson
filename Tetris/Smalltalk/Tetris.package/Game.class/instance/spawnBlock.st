action
spawnBlock
	"spawnBlock places the tetris piece in the middle top of the board"
	
	| y offset |
	
	y := ((board getDimension x) / 2) floor.
	offset := block findMin abs.
	
	block down: offset.
	block translate: (y - 1).
	
	self collisionDetection: false.
	hit ifTrue: [ 
		gameOver := true
		].
	

	
	
	