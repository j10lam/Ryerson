instance creation
readFrom: s
	"readFrom: s - accepts either a string or a ReadStream and converts input into an                      OrderedCollection"
	
	| stream stream2 sub |
	
	commands := OrderedCollection new.
	
	(s isString) ifTrue: [ 
		 	stream := s readStream.] 
		ifFalse: [
			stream := s
			].
		
	[stream atEnd] whileFalse: [
		stream2 := (stream nextLine) readStream.	
		sub := OrderedCollection new.	
		
		[stream2 atEnd] whileFalse: [ 
			sub add: (stream2 nextDelimited: Character space).
			].

		commands add: sub.
		sub := OrderedCollection new.	
		].
	
	self createGame.