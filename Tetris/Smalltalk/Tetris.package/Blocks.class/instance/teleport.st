action
teleport
	"teleport moves the block from initial to current position"
	
	| pivot |
	pivot := current at: 1.
	current := initial deepCopy.
	
	self down: (pivot y).
	self translate: (pivot x).
	
	
	