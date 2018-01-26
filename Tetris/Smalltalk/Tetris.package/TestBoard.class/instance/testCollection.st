tests
testCollection
	"Test to see if boardCollection is created properly"
	
	| anArray aBoard |
	
	anArray := #('4' '4').
	
	aBoard := OrderedCollection new.
	aBoard add: '|    |'; add: '|    |'; add: '|    |'; add: '|    |'; add: '+----+'. 
	
	b := Board new.
	b createBoard: anArray.
	
	self assert: aBoard equals: (b getBoard).

