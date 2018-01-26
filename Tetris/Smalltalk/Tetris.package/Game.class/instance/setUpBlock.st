initialization
setUpBlock
	"setupBlock instantiates the block object and determines the type of tetris block and its inital rotation"

	block := Blocks new.
	block createBlock: (dice roll) orientation: (dice roll).
	self spawnBlock.
	numPieces := numPieces + 1.