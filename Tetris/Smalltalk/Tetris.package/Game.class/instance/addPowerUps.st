action
addPowerUps
	"addPowerUps places the powerups onto the tetris board"
	
	| col row numRows|
	
	numRows := (board getDimension) y.
	
	powerups do:[:pt |	
		col := (pt at: 1) asInteger + 1.
		row := (pt at: 2) asInteger.
		row := (numRows - row) + 1.
		
		((board getBoard) at: row) at: col put: $x.
		].
	
