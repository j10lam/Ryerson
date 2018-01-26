tests
testNumberOfSpawnedPieces
	"Tests to check if number of spawned tetris pieces is correct"
	
	g := Game new.
	g readFrom: 'board 8 10
powerup 2 9
dice 1 2 7 2 2
moves ll
moves l l+..'.

	self assert: (g getNumPieces) equals: 2.
	