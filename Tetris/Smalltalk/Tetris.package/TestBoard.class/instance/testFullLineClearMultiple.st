tests
testFullLineClearMultiple
	"Test to check if any filled lines. if so, removes them from the board"
	
	| anArray aBoard emptyBoard|
	
	b := Board new.
	anArray := #('4' '4').
	aBoard := OrderedCollection new.
	emptyBoard := OrderedCollection new.
	
	aBoard add: '|    |'; add: '|cccc|'; add: '|    |'; add: '|cccc|'; add: '+----+'.
	emptyBoard add: '|    |'; add: '|    |'; add: '|    |'; add: '|    |'; add: '+----+'. 
	
	b createBoard: anArray.
	b setBoard: aBoard.
	b clearLine: true.
	
	self assert: emptyBoard equals: (b getBoard).

