module Piece
( Piece(..)
, defaultBlock
, createBlock
, tRotateRight
, tRotateLeft
, translate
, getBlockPoints
, isColliding
, hasBlockAt
, spawnBlock
, rotateBlock
) where

import Point
import Data.List
import Data.Ord

data Piece = Piece { pivot  :: Point
                   , points :: [Point]
                   , colour :: Char
                   } deriving (Show, Eq)

-- Default block with no blocks or colour
defaultBlock :: Piece
defaultBlock = instatiateBlock [] ' '

-- Private -- will create a block using the passed list of blocks and colour
instatiateBlock :: [Point] -> Char -> Piece
instatiateBlock list colour = Piece startingPoint list colour
        where startingPoint = Point 0 0

-- Creates a block pattern based on the passed number
createBlock :: Int -> Piece
createBlock shape
  | shape == 1 = instatiateBlock [Point 0 0, Point 1 0,    Point 0 1, Point 1 1]    'y'
  | shape == 2 = instatiateBlock [Point 0 0, Point (-1) 1, Point 1 0, Point 0 1]    'r'
  | shape == 3 = instatiateBlock [Point 0 0, Point (-1) 0, Point 0 1, Point 1 1]    'g'
  | shape == 4 = instatiateBlock [Point 0 0, Point (-1) 0, Point 1 0, Point (-1) 1] 'b'
  | shape == 5 = instatiateBlock [Point 0 0, Point (-1) 0, Point 1 0, Point 1 1]    'o'
  | shape == 6 = instatiateBlock [Point 0 0, Point (-1) 0, Point 1 0, Point 0 1]    'p'
  | shape == 7 = instatiateBlock [Point 0 0, Point (-1) 0, Point 1 0, Point 2 0]    'c'

-- Rotates the tetris piece right
tRotateRight :: Piece -> Piece
tRotateRight block@(Piece pivot points colour) = if (rotatable) then newPiece else block
        where newBlockPoints = map rotateRight points
              newPiece       = Piece pivot newBlockPoints colour
              rotatable      = colour /= 'y'

-- Rotates the tetris piece left
tRotateLeft :: Piece -> Piece
tRotateLeft block@(Piece pivot points colour) = if (rotatable) then newPiece else block
        where newBlockPoints = map rotateLeft points
              newPiece       = Piece pivot newBlockPoints colour
              rotatable      = colour /= 'y'

-- Moves the tetris piece
translate :: Piece -> Point -> Piece
translate (Piece pivot points colour) vector = Piece newPivot points colour
        where newPivot = pivot `pAdd` vector

-- Gets the actual coordinates of each point in the tetris piece
getBlockPoints :: Piece -> [Point]
getBlockPoints block = map addPivot blockPoints
        where addPivot    = pAdd $ pivot block
              blockPoints = points block

-- Returns true if the tetris piece is colliding with a point in the list of points or if it is out of bounds
isColliding :: Piece -> [Point] -> Int -> Int -> Bool
isColliding piece otherPoints width height = isColliding || not inBounds
        where blockPoints = getBlockPoints piece
              isColliding = any (\p -> p `elem` otherPoints) blockPoints
              inBounds    = all (\p -> (x p >= 0) && (y p >= 0) && (x p < width) && (y p < height)) blockPoints

-- Checks to see if the tetris piece has a block at a specified point
hasBlockAt :: Piece -> Point -> Bool
hasBlockAt piece point = point `elem` blockPoints
        where blockPoints = getBlockPoints piece

-- Moves the tetris block into the correct position in the board
spawnBlock :: Piece -> Int -> Int -> Piece
spawnBlock piece@(Piece pivot points colour) width height = newPiece
        where middle = ceiling (fromIntegral width / fromIntegral 2) - 1
              findMax = foldl (\acc p -> if (y p) > acc then (y p) else acc) 0 points
              row = (height - 1) - findMax
              newPiece = translate piece (Point middle row)

-- Rotates the block i amount of times
rotateBlock :: Piece -> Int -> Piece
rotateBlock piece i
  | i <= 0    = piece
  | otherwise = rotateBlock (tRotateRight piece) (i-1)

