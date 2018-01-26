module Dice
( Dice
, roll
) where

type Dice = [Int]

-- Rolls the dice sequence and returns the new dice + the element it landed on
roll :: Dice -> (Dice, Int)
roll (head:tail) = ((tail ++ [head]), head)

