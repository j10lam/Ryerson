action
translate: offset
	"translate: offset - shifts each item horizontally in current by an offset"

	current do:[:item | item setX: (item x + offset) setY: (item y)].