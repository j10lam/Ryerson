module Main
( Game(..)
, main
, readFrom
, printBoard
) where

import Test.HUnit
import Data.List.Split
import Board
import Dice
import Point
import Piece

main = do
     input <- getContents
     putStr $ show $ readFrom input

data Game = Game { board    :: Board
                 , piece    :: Piece
                 , dice     :: Dice
                 , gameover :: Bool
                 }

initGame = Game defaultBoard defaultBlock [] False

-- Reads in a string and does actions to the game based on the input
readFrom :: String -> Game
readFrom input = foldl parseAndDoCommand acc instructions
        where parseAndDoCommand = (\game instruction -> doCommand game (splitOn " " instruction))
              acc               = initGame
              instructions      = splitOn "\n" input

-- Transforms the game
doCommand :: Game -> [String] -> Game
doCommand game ("":_) = game

-- Creates  a new board
doCommand (Game _ piece dice gameover) ["board", c, r] = Game newBoard piece dice gameover
        where newBoard = createBoard (read c :: Int) (read r :: Int)

-- Adds a powerup to the board
doCommand (Game board piece dice gameover) ["powerup", c, r] = Game updatedBoard piece dice gameover
        where updatedBoard = addPowerup board (read c :: Int) (read r :: Int)

-- Creates a new dice
doCommand (Game board piece _ gameover) ("dice":numbers) = Game board piece newDice gameover
        where newDice = map (\n -> read n :: Int) numbers

-- Does actions to the game based on the users input
doCommand game@(Game board piece dice gameover) ("moves":moveCommands)
  | actions == [] = foldl goThroughActions game [' ']
  | otherwise     = foldl goThroughActions game actions
  where actions = foldl (\acc str -> acc ++ str) "" moveCommands

goThroughActions :: Game -> Char -> Game
goThroughActions game@(Game board piece dice isGameover) action
  | isGameover            = game
  | gameover newGame      = newGame
  | defaultBlock == piece = doActions newGame action
  | otherwise             = doActions game action
  where newGame           = createAndSpawnBlock game

createAndSpawnBlock :: Game -> Game
createAndSpawnBlock game@(Game board piece dice gameover) = newGame
        where (newDice1, sha) = roll $ dice
              (newDice2, rot) = roll $ newDice1
              newPiece        = spawnBlock (rotateBlock (createBlock sha) (rot-1)) (width board) (height board)
              newBoard        = incrementCount board
              newGame         = if isColliding newPiece (getBlPoints newBoard) (width newBoard) (height newBoard)
                                   then Game board piece dice True
                                   else Game newBoard newPiece newDice2 False

-- Does actions in the game
doActions :: Game -> Char -> Game
doActions game@(Game board piece dice gameover) 'l' = newGame
        where newBlock = translate piece $ Point (-1) 0
              newGame  = if isColliding newBlock (getBlPoints board) (width board) (height board)
                            then game
                            else Game board newBlock dice gameover

doActions game@(Game board piece dice gameover) 'r' = newGame
        where newBlock = translate piece $ Point 1 0
              newGame  = if isColliding newBlock (getBlPoints board) (width board) (height board)
                            then game
                            else Game board newBlock dice gameover

doActions game@(Game board piece dice gameover) 'L' = newGame
        where newBlock = tRotateLeft piece
              newGame  = if isColliding newBlock (getBlPoints board) (width board) (height board)
                            then game
                            else Game board newBlock dice gameover

doActions game@(Game board piece dice gameover) 'R' = newGame
        where newBlock = tRotateRight piece
              newGame  = if isColliding newBlock (getBlPoints board) (width board) (height board)
                            then game
                            else Game board newBlock dice gameover

doActions game@(Game board piece dice gameover) '.' = newGame
        where newBlock = translate piece $ Point 0 (-1)
              newBoard = removeRow (addTetrisBlock board (getBlockPoints piece) (colour piece)) (height board)
              powBoard = removePowerRows board (findPowerUpLines board 1)
              newGame  = if isColliding newBlock (getBlPoints board) (width board) (height board)
                            then createAndSpawnBlock (Game newBoard defaultBlock dice gameover)
                            else if isColliding newBlock (getPwPoints board) (width board) (height board)
                                    then Game powBoard newBlock dice gameover
                                    else Game board newBlock dice gameover

doActions game@(Game board piece dice gameover) '+'
        | defaultBlock == piece = createAndSpawnBlock game
        | otherwise             = newGame
        where newBlock = translate piece $ Point 0 (-1)
              newBoard = removeRow (addTetrisBlock board (getBlockPoints piece) (colour piece)) (height board)
              newGame  = if isColliding newBlock (getBlPoints board) (width board) (height board)
                            then doActions (Game newBoard defaultBlock dice gameover) '+'
                            else doActions (Game board newBlock dice gameover) '+'

doActions game ' ' = game

-- Converts the board into a list of Strings for each row
printBoard :: Board -> [String]
printBoard board@(Board wi he bl pl count)
          | he == 0       = []
          | otherwise     = [rowString] ++ printBoard (Board wi (he - 1) bl pl count)
          where rowNum    = he - 1
                getPoint  = (\c -> Point c rowNum)
                getLetter = (\c -> getCharAt board $ getPoint c)
                row       = concat $ [[getLetter c] | c <- [0..(wi-1)]]
                rowString = "|" ++ row ++ "|"

-- Formats the board for printing
formatBoard :: Board -> Piece -> Bool -> String
formatBoard board piece isGameOver =  unlines (newRow1:rest) ++ bottomRow
        where piecePoints = getBlockPoints piece
              newBoard    = if not isGameOver then addTetrisBlock board piecePoints $ colour piece
                                              else board
              (row1:rest) = printBoard newBoard
              countString = printCount $ count board
              newRow1     = row1 ++ countString
              bottomRow   = "+" ++ replicate (width board) '-' ++ "+\n"

-- Returns a string saying how many pieces were dropped
printCount :: (Integral a, Show a) => a -> String
printCount x
  | x == 1    = " 1 piece"
  | otherwise = " " ++ (show x) ++ " pieces"

instance Show Game where
        show (Game board piece _ gameover) = formatBoard board piece gameover

tests = test [
--  testSimpleEmpty
        "tiny empty board" ~:
          "|       | 0 pieces\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \+-------+\n" ~=?
        (show $ readFrom "board 7 4")

        ,"larger empty board" ~:
          "|        | 0 pieces\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 6")

        ,"odd-size board with powerups" ~:
          "|       | 0 pieces\n\
          \|  x    |\n\
          \|       |\n\
          \| x     |\n\
          \+-------+\n\
          \" ~=?
        (show $ readFrom "board 7 4\n\
                         \powerup 3 3\n\
                         \powerup 2 1")

--  testSimpleEvenWidth
        ,"podium" ~:
          "|   p    | 1 piece\n\
          \|  ppp   |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 6\n\
                         \dice 6 1\n\
                         \moves")

        ,"podium rotated" ~:
          "|   p    | 1 piece\n\
          \|   pp   |\n\
          \|   p    |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 6\n\
                         \dice 6 2\n\
                         \moves")

        ,"green piece" ~:
          "|   gg   | 1 piece\n\
          \|  gg    |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 6\n\
                         \dice 3 1\n\
                         \moves")

        ,"green rotated" ~:
          "|   g    | 1 piece\n\
          \|   gg   |\n\
          \|    g   |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 6\n\
                         \dice 3 2\n\
                         \moves ")

     ,"upside-w" ~:
           "|   gg   | 1 piece\n\
           \|  gg    |\n\
           \|        |\n\
           \|        |\n\
           \|        |\n\
           \|        |\n\
           \+--------+\n\
           \" ~=?
         (show $ readFrom "board 8 6\n\
                         \dice 3 3\n\
                         \moves R")

        ,"green can rotate" ~:
          "|   g    | 1 piece\n\
          \|   gg   |\n\
          \|    g   |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 6\n\
                         \dice 3 1\n\
                         \moves R")

        ,"2 pieces" ~:
          "|   c    | 2 pieces\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|   yy   |\n\
          \|   yy   |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 10\n\
                         \dice 1 2 7 2 2\n\
                         \moves +")

        ,"cyan unrotated" ~:
          "|  cccc  | 2 pieces\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|   yy   |\n\
          \|   yy   |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 10\n\
                         \dice 1 1 7 1 2\n\
                         \moves +")

        ,"3 pieces" ~:
          "|  rr    | 3 pieces\n\
          \|   rr   |\n\
          \|        |\n\
          \|        |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   yy   |\n\
          \|   yy   |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 10\n\
                         \dice 1 2 7 2 2\n\
                         \moves ++")

        ,"2 pieces with powerup" ~:
          "|        | 2 pieces\n\
          \| x      |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|        |\n\
          \|        |\n\
          \|yy      |\n\
          \|yy      |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 10\n\
                         \powerup 2 9\n\
                         \dice 1 2 7 2 2\n\
                         \moves ll ll\n\
                         \moves +..")

        ,"2 pieces with powerup hidden" ~:
          "|        | 2 pieces\n\
          \| c      |\n\
          \| c      |\n\
          \| c      |\n\
          \| c      |\n\
          \|        |\n\
          \|        |\n\
          \|        |\n\
          \|yy      |\n\
          \|yy      |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 10\n\
                         \powerup 2 9\n\
                         \dice 1 2 7 2 2\n\
                         \moves ll ll\n\
                         \moves +ll.")


--  testSimpleOddWidth
        ,"odd green" ~:
          "|   gg  | 1 piece\n\
          \|  gg   |\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \+-------+\n\
          \" ~=?
        (show $ readFrom "board 7 6\n\
                         \dice 3 1\n\
                         \moves")

        ,"odd green rotated" ~:
          "|   g   | 1 piece\n\
          \|   gg  |\n\
          \|    g  |\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \+-------+\n\
          \" ~=?
        (show $ readFrom "board 7 6\n\
                         \dice 3 2\n\
                         \moves ")

        ,"odd 2 pieces" ~:
          "|   c   | 2 pieces\n\
          \|   c   |\n\
          \|   c   |\n\
          \|   c   |\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \|   yy  |\n\
          \|   yy  |\n\
          \+-------+\n\
          \" ~=?
        (show $ readFrom "board 7 10\n\
                         \dice 1 2 7 2 2\n\
                         \moves +")

        ,"odd 2 cyan horizontal" ~:
          "|  cccc | 2 pieces\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \|       |\n\
          \|   yy  |\n\
          \|   yy  |\n\
          \+-------+\n\
          \" ~=?
        (show $ readFrom "board 7 10\n\
                         \dice 1 1 7 1 2\n\
                         \moves +")

        ,"odd 3 pieces" ~:
          "|  rr   | 3 pieces\n\
          \|   rr  |\n\
          \|       |\n\
          \|       |\n\
          \|   c   |\n\
          \|   c   |\n\
          \|   c   |\n\
          \|   c   |\n\
          \|   yy  |\n\
          \|   yy  |\n\
          \+-------+\n\
          \" ~=?
        (show $ readFrom "board 7 10\n\
                         \dice 1 2 7 2 2\n\
                         \moves ++")


--  testMultipiece
        ,"4 pieces" ~:
          "|   gg  | 4 pieces\n\
          \|  gg   |\n\
          \|   c   |\n\
          \|   c   |\n\
          \|   c   |\n\
          \|   c   |\n\
          \|  rr   |\n\
          \|   rr  |\n\
          \|   gg  |\n\
          \|  gg   |\n\
          \+-------+\n\
          \" ~=?
        (show $ readFrom "board 7 10\n\
                         \dice 3 1 2 1 7 2\n\
                         \moves +++++++++++")

        ,"20 pieces" ~:
          "|        | 20 pieces\n\
          \|        |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 10\n\
                         \dice 7 2\n\
                         \moves r+ rr+ rrr+ rrrr+ l+ ll+ lll+ Rrrrrr+ rrrr+ rrrr+ rrrr+ rrrr+ + Rllll+ lll+ ll+ l+  +++++++")

        ,"14 pieces" ~:
          "|   c    | 14 pieces\n\
          \|   c    |\n\
          \|   c    |\n\
          \|  xc    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|   c    |\n\
          \|cccc    |\n\
          \|cccc    |\n\
          \|cccc    |\n\
          \+--------+\n\
          \" ~=?
        (show $ readFrom "board 8 10\n\
                         \dice 7 2\n\
                         \powerup 3 7\n\
                         \moves r+ rr+ rrr+ rrrr+ l+ ll+ lll+ l....r +Rrrrr+lll+ll+l++++")]

