initialization
createGame
	"createGame instantiates instance variables and calls startGame to begin Tetris."

	moveList := OrderedCollection new.
	powerups := OrderedCollection new.
	numPieces := 0.
	gameOver := false.
	
	commands do: [:line |
		(line first = 'board') ifTrue: [ 
			board := Board new.
			board createBoard: (line removeFirst; asArray)].
		
		(line first = 'powerup') ifTrue: [ 
			powerups add: (line removeFirst; asArray).
			self addPowerUps.
			].
		
		(line first = 'dice') ifTrue: [ 
			dice := Dice new.
			dice setRoll: (line removeFirst; asArray)].
		
		(line first ='moves') ifTrue: [ 
			line removeFirst.
			moveList := moveList, line.
			].
		].
	self startGame.