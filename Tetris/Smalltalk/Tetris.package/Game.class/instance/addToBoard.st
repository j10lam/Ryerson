action
addToBoard
	"addToBoard adds the tetris block onto the board"
	
	(block getBlock) do:[:pt |
		((board getBoard) at: (pt y + 1)) at: (pt x + 2) put: (block getLetter).
		].
	
		
	