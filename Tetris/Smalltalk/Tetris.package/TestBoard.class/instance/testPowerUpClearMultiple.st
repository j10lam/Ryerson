tests
testPowerUpClearMultiple
	"Test to check if any lines with only one cell empty. if so, removes last occurence from the board"
	
	| anArray aBoard emptyBoard|
	
	b := Board new.
	anArray := #('4' '4').
	aBoard := OrderedCollection new.
	emptyBoard := OrderedCollection new.
	
	aBoard add: '|    |'; add: '|    |'; add: '|c cc|'; add: '|c cc|'; add: '+----+'.
	emptyBoard add: '|    |'; add: '|    |'; add: '|c cc|'; add: '|    |'; add: '+----+'. 
	
	b createBoard: anArray.
	b setBoard: aBoard.
	b clearLine: false.
	
	self assert: emptyBoard equals: (b getBoard).

