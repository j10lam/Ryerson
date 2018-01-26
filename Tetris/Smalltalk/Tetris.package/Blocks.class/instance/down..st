action
down:offset
	"down: offset - increases the y value of each cell in the block by an offset"
	
	current do:[:item | item setX: (item x) setY: (item y + offset)].