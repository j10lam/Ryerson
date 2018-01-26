tests
testLineSpawnCorrectly
 	"Test to see if the line piece is placed properly (Ex. pivot is placed on 2nd row)"

	g:=Game new.
	g readFrom: 'board 5 5
dice 7 2
moves lr'.
	b := g getBoard.
	
	self assert: ((b occurrencesOf: '| c   |') = 4).
	