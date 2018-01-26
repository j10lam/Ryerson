initialization
createBlock: choice orientation: o
	"createBlock: choice orientation:o - instantiates a tetris block object with an initial                orientation.
	 choice = tetris piece type
	 o = initial orientation (rotated state)"
	
	initial := OrderedCollection new.
	frozen := false.

 	(choice = '1') ifTrue: [
		initial add: 0@0; add: 0@(-1); add: 1@(-1); add: 1@0.
		letter := $y].
	(choice = '2') ifTrue: [ 
		initial add: 0@0; add: 1@0; add: 0@(-1); add: -1@(-1).
		letter := $r].
	(choice = '3') ifTrue: [ 
		initial add: 0@0; add: -1@0; add: 0@(-1); add: 1@(-1).
		letter := $g].
	(choice = '4') ifTrue: [
		initial add: 0@0; add: 1@0; add: -1@0; add: -1@(-1).
		letter := $b].
	(choice = '5') ifTrue: [ 
		initial add: 0@0; add: -1@0; add: 1@0; add: 1@(-1).
		letter := $o].
	(choice = '6') ifTrue: [ 
		initial add: 0@0; add: -1@0; add: 1@0; add: 0@(-1).
		letter := $p].
	(choice = '7') ifTrue: [ 
		initial add: 0@0; add: -1@0; add: 1@0; add: 2@0.
		letter := $c].
	
	current := initial deepCopy.
	(o asInteger - 1) timesRepeat: [ 
		self rotate: 'R' ].
	
