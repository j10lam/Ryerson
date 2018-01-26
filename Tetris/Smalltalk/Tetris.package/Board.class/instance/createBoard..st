initialization
createBoard: dimensions
	"createBoard: dimensions - creates a blank tetris board of size: cols, rows from dimension"
	| bottom |
	
	cols := (dimensions at: 1) asInteger.
	rows := (dimensions at: 2) asInteger.
	template := OrderedCollection new.
	
	bottom := '+', ('-' repeat: cols), '+'.
	emptyRow := '|', (' ' repeat: cols), '|'.
	
	1 to: rows do: [ :i |
		template add: ('|', (' ' repeat: cols), '|').
	].

	template addLast: bottom.


