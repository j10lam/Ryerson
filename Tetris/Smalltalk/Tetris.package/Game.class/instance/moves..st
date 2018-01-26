action
moves: command
	"moves: command - moves a tetris piece by the given command
	 and checks to see if move is possible or block is frozen"
	
	block saveState.
	(command = 'l') ifTrue: [
		block translate: -1].
	(command = 'L') ifTrue: [
		block rotate: 'L'].
	(command = 'r') ifTrue: [
		block translate: 1].	
	(command = 'R') ifTrue: [
		block rotate: 'R'].
	(command = '+') ifTrue: [
		[block isFrozen] whileFalse: [ 
			block down: 1.
		
			self collisionDetection: true.
			(hit = true) ifTrue: [ 
				block revertState].
			self checkBelow.
		].
	].
	(command = '.') ifTrue: [
		block down: 1.].
	
	self collisionDetection: false.
	(hit = true) ifTrue: [ 
		block revertState].
	self checkBelow.
