module Board
( Board(..)
, defaultBoard
, createBoard
, addPowerup
, getCharAt
, addTetrisBlock
, incrementCount
, getBlPoints
, getPwPoints
, removeRow
, removePowerRows
, findPowerUpLines
) where

import Point

data Board = Board { width  :: Int
                   , height :: Int
                   , blList :: [(Point, Char)]
                   , pwList :: [(Point, Char)]
                   , count  :: Int
                   } deriving (Show)

-- Returns a board with default properties
defaultBoard :: Board
defaultBoard = Board 0 0 [] [] 0

-- Returns a board with a new width and height
createBoard :: Int -> Int -> Board
createBoard c r = Board c r [] [] 0

-- Adds a powerup into the board
addPowerup :: Board -> Int -> Int -> Board
addPowerup (Board wi he bls pws count) c r = Board wi he bls updatedPws count
        where newPowerup = (Point (c-1) (r-1), 'x')
              updatedPws = pws ++ [newPowerup]

-- Adds the points from a tetris block into the board
addTetrisBlock :: Board -> [Point] -> Char -> Board
addTetrisBlock (Board wi he bls pws count) points colour = Board wi he updatedBlockList pws count
        where newBlocks = map (\p -> (p, colour)) points
              updatedBlockList = bls ++ newBlocks

-- Increments the number of spawned tetris blocks in the board by 1
incrementCount :: Board -> Board
incrementCount (Board wi he bls pws count) = Board wi he bls pws newCount
        where newCount = count + 1

getBlPoints :: Board -> [Point]
getBlPoints board = map toPoint $ blList board
        where toPoint = (\(p, _) -> p)

getPwPoints :: Board -> [Point]
getPwPoints board = map toPoint $ pwList board
        where toPoint = (\(p, _) -> p)

-- Gets the blocks at at a row index
getBlocksAtRow :: Board -> Int -> [(Point, Char)]
getBlocksAtRow board rowNumber = blocksInRow
        where sameRow     = (\(p, _) -> (y p) == rowNumber)
              blocks      = blList board
              blocksInRow = filter sameRow blocks

-- Gets the number of blocks at a row
numberOfBlocksAtRow :: Board -> Int -> Int
numberOfBlocksAtRow board rowNumber = length $ getBlocksAtRow board rowNumber

-- Gets the colour/character at a specific point in a board
getCharAt :: Board -> Point -> Char
getCharAt board point = if (blockChar /= ' ') then blockChar else powerupChar
        where blockList   = blList board
              powerupList = pwList board
              blockChar   = getCharHelper point blockList
              powerupChar = getCharHelper point powerupList

-- Helps the getChar function by searching a point recursively
getCharHelper :: Point -> [(Point, Char)] -> Char
getCharHelper _ [] = ' '
getCharHelper point ((frozenPoint, colour):rest)
  | point == frozenPoint = colour
  | otherwise            = getCharHelper point rest

-- Removes all the full rows in the board
removeRow :: Board -> Int -> Board
removeRow board (-1) = board
removeRow board@(Board wi he bls pws count) r = removeRow newBoard $ r-1
        where full               = (\l -> l == wi)
              numBlocks          = numberOfBlocksAtRow board r
              removeAndShiftRows = (\blockList -> shiftRows (removeBlocks blockList r) r)
              newBls             = if (full numBlocks) then removeAndShiftRows bls
                                                       else bls
              newBoard           = Board wi he newBls pws count

-- Removes all the rows that that were passed in the index list
removePowerRows :: Board -> [Int] -> Board
removePowerRows board [] = board
removePowerRows (Board wi he bls pws count) (r:rest) = removePowerRows newBoard updatedIndexes
        where newBls         = shiftRows (removeBlocks bls r) r
              updatedIndexes = map (+ (-1)) rest
              newBoard       = Board wi he newBls pws count

-- Finds all the indexs of rows that are missing 1 block and returns the first 'numTriggered' indexes
findPowerUpLines :: Board -> Int -> [Int]
findPowerUpLines board numTriggered = take numTriggered indexes
        where rows           = (height board) - 1
              cols           = (width board) - 1
              numberOfBlocks = numberOfBlocksAtRow board
              isOneMissing   = (\l -> l == cols)
              indexes        = filter (\r -> (isOneMissing $ numberOfBlocks r)) [0..rows]

-- Removes all the blocks that are in the passed row index
removeBlocks :: [(Point, Char)] -> Int -> [(Point, Char)]
removeBlocks [] _ = []
removeBlocks (block:rest) r = newList
        where isSameRow  = (\point -> (y point) == r)
              (point, _) = block
              newList    = if (not $ isSameRow point) then block:(removeBlocks rest r)
                                                      else removeBlocks rest r

-- Moves all the blocks above the passed row index down by 1 row
shiftRows :: [(Point, Char)] -> Int -> [(Point, Char)]
shiftRows bls row = map moveIfAboveRow bls
        where movePointDown  = pAdd (Point 0 (-1))
              moveIfAboveRow = (\(p, c) -> if ((y p) > row) then (movePointDown p, c)
                                                            else (p, c))

