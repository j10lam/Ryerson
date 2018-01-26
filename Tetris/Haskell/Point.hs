module Point 
( Point(..)
, pAdd
, rotateRight
, rotateLeft
) where

-- Creates a Type that will contain a x and y coordinate and allows it to be checked for equality
data Point = Point { x :: Int
                   , y :: Int
                   } deriving (Show, Eq)

-- Add two points together
pAdd :: Point -> Point -> Point
pAdd p1 p2 = Point {x=(x p1 + x p2), y=(y p1 + y p2)}

-- Rotates the point right around the (0,0) axis
rotateRight :: Point -> Point
rotateRight point = Point {x=(y point), y=(negate $ x point)}

-- Rotates the point left around the (0,0) axis
rotateLeft :: Point -> Point
rotateLeft point = Point {x=(negate $ y point), y=(x point)}

