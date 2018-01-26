defmodule Assign2Test do
  use ExUnit.Case
  doctest Assign2
  import Assign2

  test "4x4 board" do
    assert readFrom("board 4 4") |> print() ==
"|    | 0 pieces
|    |
|    |
|    |
+----+
"
  end

  test "A powerup" do
    assert readFrom("board 4 4
powerup 3 4") |> print() ==
"|  x | 0 pieces
|    |
|    |
|    |
+----+
"
  end

  test "Multiple powerups" do
    assert readFrom("board 4 4
powerup 3 4
powerup 2 2") |> print() ==
"|  x | 0 pieces
|    |
| x  |
|    |
+----+
"
  end

  test "Square even spawn" do
    assert readFrom("board 4 4
dice 1 1") |> print() ==
"| yy | 1 pieces
| yy |
|    |
|    |
+----+
"
  end

  test "Square odd spawn" do
    assert readFrom("board 3 4
dice 1 1") |> print() ==
"| yy| 1 pieces
| yy|
|   |
|   |
+---+
"
  end

  test "Rotated square" do
    assert readFrom("board 4 4
dice 1 2") |> print() ==
"| yy | 1 pieces
| yy |
|    |
|    |
+----+
"
  end

  test "Line" do
    assert readFrom("board 4 4
dice 7 1") |> print() ==
"|cccc| 1 pieces
|    |
|    |
|    |
+----+
"
  end

  test "Cannot rotate line" do
    assert readFrom("board 5 5
dice 7 1
moves R") |> print() ==
"| cccc| 1 pieces
|     |
|     |
|     |
|     |
+-----+
"
  end

  test "Rotated line spawn - to test offseted spawn" do
    assert readFrom("board 4 4
dice 7 2") |> print() ==
"| c  | 1 pieces
| c  |
| c  |
| c  |
+----+
"
  end

  test "T block" do
    assert readFrom("board 4 4
dice 6 1") |> print() ==
"| p  | 1 pieces
|ppp |
|    |
|    |
+----+
"
  end

  test "Clockwise rotated T block" do
    assert readFrom("board 4 4
dice 6 1
moves R") |> print() ==
"| p  | 1 pieces
| pp |
| p  |
|    |
+----+
"
  end

  test "Counterclockwise rotated T block" do
    assert readFrom("board 4 4
dice 6 1
moves L") |> print() ==
"| p  | 1 pieces
|pp  |
| p  |
|    |
+----+
"
  end

  test "Upside-down T block" do
    assert readFrom("board 4 4
dice 6 1
moves RR") |> print() ==
"|    | 1 pieces
|ppp |
| p  |
|    |
+----+
"
  end

  test "Square move left" do
    assert readFrom("board 4 4
dice 1 1
moves l") |> print() ==
"|yy  | 1 pieces
|yy  |
|    |
|    |
+----+
"
  end

  test "Check left boundary" do
    assert readFrom("board 4 4
dice 1 1
moves llllllll") |> print() ==
"|yy  | 1 pieces
|yy  |
|    |
|    |
+----+
"
  end

  test "Square move right" do
    assert readFrom("board 4 4
dice 1 1
moves r") |> print() ==
"|  yy| 1 pieces
|  yy|
|    |
|    |
+----+
"
  end


  test "Check right boundary" do
    assert readFrom("board 4 4
dice 1 1
moves rrrrrrrr") |> print() ==
"|  yy| 1 pieces
|  yy|
|    |
|    |
+----+
"
  end

  test "Square move down" do
    assert readFrom("board 4 4
dice 1 1
moves .") |> print() ==
"|    | 1 pieces
| yy |
| yy |
|    |
+----+
"
  end

  test "Square fall" do
    assert readFrom("board 4 5
dice 1 1
moves +") |> print() ==
"| yy | 2 pieces
| yy |
|    |
| yy |
| yy |
+----+
"
  end


  test "Cannot spawn a rotated line" do
    assert readFrom("board 4 5
dice 1 1 7 2
moves +") |> print() ==
"|    | 1 pieces
|    |
|    |
| yy |
| yy |
+----+
"
  end

  test "Square at bottom" do
    assert readFrom("board 4 4
dice 1 1
moves ..") |> print() ==
"|    | 1 pieces
|    |
| yy |
| yy |
+----+
"
  end

  test "Spawn new block" do
    assert readFrom("board 4 5
dice 1 1
moves ....") |> print() ==
"| yy | 2 pieces
| yy |
|    |
| yy |
| yy |
+----+
"
  end

  test "GameOver" do
    assert readFrom("board 4 6
dice 1 1 7 2
moves +.....") |> print() ==
"| c  | 2 pieces
| c  |
| c  |
| c  |
| yy |
| yy |
+----+
"
  end

  test "Clear filled lines #1" do
    assert readFrom("board 5 5
dice 7 1 7 2
moves +lll+") |> print() ==
"| cccc| 3 pieces
|     |
|c    |
|c    |
|c    |
+-----+
"
  end

  test "Clear filledlines #2" do
    assert readFrom("board 6 10
dice 7 2
moves ll+l+r+rr+rrr++") |> print() ==
"|  c   | 7 pieces
|  c   |
|  c   |
|  c   |
|      |
|      |
|      |
|      |
|      |
|      |
+------+
"
  end

  test "Powerup clear" do
    assert readFrom("board 5 5
dice 1 1
powerup 2 3
moves ll+r+l.") |> print() ==
"|     | 3 pieces
| yy  |
| yy  |
|     |
|yy yy|
+-----+
"
  end

    test "Given example" do
      assert readFrom("board 8 10
powerup 2 9
dice 1 2 7 2 2
moves ll
moves l l+..
") |> print() ==
"|        | 2 pieces
| x      |
|   c    |
|   c    |
|   c    |
|   c    |
|        |
|        |
|yy      |
|yy      |
+--------+
"
    end

    test "20 pieces" do
      assert readFrom("board 8 10
dice 7 2
moves r+ rr+ rrr+ rrrr+ l+ ll+ lll+ Rrrrrr+ rrrr+ rrrr+ rrrr+ rrrr+ + Rllll+ lll+ ll+ l+  +++++++")
|> print() ==
"|        | 20 pieces
|        |
|   c    |
|   c    |
|   c    |
|   c    |
|   c    |
|   c    |
|   c    |
|   c    |
+--------+
"
    end

    test "14 pieces" do
      assert readFrom("board 8 10
dice 7 2
powerup 3 7
moves r+ rr+ rrr+ rrrr+ l+ ll+ lll+ l....r +Rrrrr+lll+ll+l++++") |>
print() ==
"|   c    | 14 pieces
|   c    |
|   c    |
|  xc    |
|   c    |
|   c    |
|   c    |
|cccc    |
|cccc    |
|cccc    |
+--------+
"
    end

end
