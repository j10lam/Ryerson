tests
testA1Example
	"Tests the given example to see if output is the same"
	
	| output |
	g := Game new.
	g readFrom: 'board 8 10
powerup 2 9
dice 1 2 7 2 2
moves ll
moves l l+..'.

	output := OrderedCollection new.
	output add: '|        |'; add: '| x      |'; add: '|   c    |'; add: '|   c    |'; 
	add: '|   c    |'; add: '|   c    |'; add: '|        |'; add: '|        |'; add: '|yy      |';
	add: '|yy      |'; add: '+--------+'.
	
	self assert: output equals: (g getBoard).
	