printing
printOn: aWriteStream
	"printOn: aWriteStream - prints the tetris board onto a WriteStream"
	
	| boardState first|
	
	boardState := board getBoard.
	first := true.
	
	boardState do: [: r |
		aWriteStream nextPutAll: r.
		
		(first) ifTrue: [
			aWriteStream nextPutAll: ' ', (numPieces asString), ' pieces'.
			first := false.
			].

		aWriteStream cr].
	
	aWriteStream flush.