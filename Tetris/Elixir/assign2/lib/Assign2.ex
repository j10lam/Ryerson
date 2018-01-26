defmodule Assign2 do
  @moduledoc """
  This module parses a string of commands and outputs the final tetris board
  """
  import String, only: [to_integer: 1]
  import Block
  import Frozen
  import Board

  @newline "
"

  @doc """
  readFrom(aString) parses a given string into a list of tuples.
                    Each tuple contains info regarding: dice, board, moves, etc.
  parameters:
    aString - commands as a string
  return: a list of (atom, tuples)
  """
  def readFrom(aString) do
    init() |>
      readFrom(aString)
  end

  @doc """
  init() creates a list of tuples to hold info regarding the game
  return: a list of (atom, tuples)
  """
  def init() do
    {:game, {}, [], ["x"], []}
  end

  @doc """
  readFrom(aGame, aString) parses a given string into a list of tuples.
                    Each tuple contains info regarding: dice, board, moves, etc.
  parameters:
    aGame - container for respective info {_, board, dice, powerups, commands}
    aString - commands as a string
  return: a list of (atom, tuples)
  """
  def readFrom(aGame, aString) do
    List.foldl(String.split(aString, @newline),
               aGame,
               &(doCommand(String.split(&1, " "), &2))) |>

    gameHandler()
  end

  @doc """
  doCommand([""_], aGame) pattern matches for an empty string as the first item
  parameters:
    aGame - ontainer for respective info {_, board, dice, powerups, commands}
  return: aGame (a list of (atom, tuples))
  """
  def doCommand([""|_], aGame), do: aGame

  @doc """
  doCommand(["board", c, r], {:game, _, dice, powerups, commands})
           pattern matches for the string "board" as the first item
  parameters:
    c - number of columns
    r - number of rows
    dice, powerups, commands - lists
  return: a list of (atom, tuples)
  """
  def doCommand(["board", c, r], {:game, _, dice, powerups, commands}) do
    rows = to_integer(r)
    cols = to_integer(c)

    {:game, {cols, rows}, dice, powerups, commands}
  end

  @doc """
  doCommand(["dice"|tail], {:game, board, _, powerups, commands})
           pattern matches for the string "dice" as the first item
  parameters:
    tail - all but the first item in the list
    board - tuples
    dice - powerups, commands - lists
  return: a list of (atom, tuples)
  """
  def doCommand(["dice"|tail], {:game, board, dice, powerups, commands}) do
    asIntegers = Enum.map(tail, fn(n) -> to_integer(n) end)

    {:game, board, dice++asIntegers, powerups, commands}
  end

  @doc """
  doCommand(["powerup",c, r], {:game, board, dice, powerups, commands})
           pattern matches for the string "powerup" as the first item
  parameters:
    c - column
    r - row
    board - list
    dice, powerups, commands - lists
  return: a list of (atom, tuples)
  """
  def doCommand(["powerup", c, r], {:game, board, dice, powerups, commands}) do
    x = to_integer(c) - 1
    y = to_integer(r) - 1
    powerup = {x, y}

    {:game, board, dice, List.insert_at(powerups, -1, powerup), commands}
  end

  @doc """
  doCommand(["moves"|tail], {:game, board, dice, powerups, commands})
           pattern matches for the string "moves" as the first item
  parameters:
    tail - all but the first item in the list
    board - tuple
    dice, powerups, commands - lists
  return: a list of (atom, tuples)
  """
  def doCommand(["moves"|tail], {:game, board, dice, powerups, commands}) do
    tail = List.to_string(tail) |> String.codepoints()
    {:game, board, dice, powerups, (commands ++ tail)}
  end

  @doc """
  moves(:gamOver, frozen, num) Base case. Called when a gameover state reached
  parameters:
    frozen - a list of maps containing frozen blocks
    num - the number of blocks spawned on the board
  return: a list containing: frozen, num
  """
  def moves(:gameOver, frozen, num) do
    [frozen, num]
  end

  @doc """
  moves([], _, block,frozen, _, _, num) Base case. When moves are all consumed
  parameters:
    block - current tetris block
    frozen - a list of maps containing frozen blocks
    num - the number of blocks spawned on the board
  return: a list containing: frozen, num
  """
  def moves([], _, block,frozen, _, _, num) do
    num = num + 1
    frozen = getBlock(block) |> addBlock(frozen)
    [frozen, num]
  end

  @doc """
  moves([command|rest], dice, block, frozen, powerups, {c,r}, num) modifies a
    block given a command, checks collisions, creates new blocks and recursively
    calls itself until all commands are consumed or gameover reached.
  parameters:
    command - the current command as String
    rest - list of commands
    dice - the dice sequence (list of numbers)
    block - current tetris block
    frozen - a list of maps containing frozen blocks
    powerups - the list of powerups (list of tuples)
    {c,r} - columns, rows respectively
    num - the number of blocks spawned on the board
  return: a list containing: frozen, num
  """
  def moves([command|rest], dice, block, frozen, powerups, {c,r}, num) do
    newBlock = case command do
      "r" -> translate(block, 1)
      "l" -> translate(block, -1)
      "R" -> rotate(block, "R", 2)
      "L" -> rotate(block, "L", 2)
      "." -> down(block, 1)
      "+" -> down(block, 1)
    end
    [block, frozen, stuck] =
      ops(block, frozen, powerups, {c,r}, newBlock, command)

    if ((command == "." or command == "+") and stuck) do
      command = :default
      frozen = addBlock(getBlock(block), frozen)
      [dice,block] = setupBlock(dice, {c,r})
      num = num + 1
      frozen = clearLine(1, frozen, c, :full)
    end

    if collisionDetection(:collision, getBlock(block), frozen) do
      moves(:gameOver, frozen, num)
    else
      unless(command == "+") do
        moves(rest, dice, block, frozen, powerups, {c,r}, num)
      else
        moves([command|rest], dice, block, frozen, powerups, {c,r}, num)
      end
    end
  end


  @doc """
  gameHandler({:game, {c,r}, [], powerups, commands}) runs the tetris game
  parameters:
    command - the current command as String
    powerups - the list of powerups (list of tuples)
    {c,r} - columns, rows respectively
  return: a list
  """
  def gameHandler({:game, {c,r}, [], powerups, commands}) do
    frozen = [] ++ [List.duplicate(0, r)]
    [frozen, 0, powerups, {c,r}]
  end

  @doc """
  gameHandler({:game, {c,r}, dice, powerups, commands}) runs the tetris game
  parameters:
    command - the current command as String
    dice - the dice sequence (list of numbers)
    powerups - the list of powerups (list of tuples)
    {c,r} - columns, rows respectively
  return: a list
  """
  def gameHandler({:game, {c,r}, dice, powerups, commands}) do

    frozen = [] ++ [List.duplicate(0, r)]
    num = 0
    [dice,block] = setupBlock(dice, {c,r})

    [frozen, num] =
    if collisionDetection(:collision, getBlock(block), frozen) do
      moves(:gameOver, frozen, num)
    else
      moves(commands, dice, block, frozen, powerups, {c,r}, num)
    end

    [frozen, num, powerups, {c,r}]
  end

  @doc """
  ops(block, frozen, powerups, {c,r}, newBlock, command) checks if the move
    command is valid
  parameters:
    command - the current command as String
    block - current tetris block
    powerups - the list of powerups (list of tuples)
    {c,r} - columns, rows respectively
    newBlock - a block that has been trasnformed by moves
  return: a list
  """
  def ops(block, frozen, powerups, {c,r}, newBlock, command) do
    stuck = true
    transformed = getBlock(newBlock)

    a = bounds(transformed, {c,r})
    b = collisionDetection(:collision, transformed, frozen)

    if !(a or b) do
      stuck = false
      block = newBlock
    end

    if (command == ".") do
      frozen = collisionDetection(:pcollision, getBlock(block), powerups) |>
      clearLine(frozen, c, :powerClear)
    end

    [block, frozen, stuck]
  end

  @doc """
  collisionDetection(:collision, block, [_|frozen]) checks if a collision occured
  parameters:
    :collision - atom representing block-block collisions
    block - current tetris block
    frozen - list of frozen blocks
  return: a bool
  """
  def collisionDetection(:collision, block, [_|frozen]) do
    pixels = toList(block)
    fPixels = toList(frozen)

    length(pixels -- fPixels) < length(pixels)
  end

  @doc """
  collisionDetection(:pcollision, block, powerups) checks if a collision with a
    powerup has occured
  parameters:
    :pcollision - atom representing block-powerup collisions
    block - current tetris block
    powerups - list of powerups
  return: the number of powerups triggered
  """
  def collisionDetection(:pcollision, block, powerups) do
    pixels = toList(block)

    numPowerups = length(powerups)

    diff = (powerups -- pixels) |> length()

    (numPowerups - diff)
  end

  @doc """
  bounds(block, {c,r}) checks to see if the block is out of bounds
  parameters:
    block - current tetris block
    {c,r} - columns and rows of board respectively
  return: a bool
  """
  def bounds(block, {c,r}) do
    Enum.any?(block, fn(p) -> (p.x == -1) or (p.x == c) or
                              (p.y == -1) or (p.y == r) end)
  end

  @doc """
  print([[count|frozen], num, powerups, {c,r}]) prints the current state of the
    tetris board as a String
  parameters:
    frozen - the list of frozen blocks
    num - the number of spawned tetris blocks
    powerups - a list of powerup coordinates
    {c,r} - the columns and rows of the board respectively
  return: a String representing the current board state
  """
  def print([[_|frozen], num, powerups, {c,r}]) do
    board = createBoard({c,r})
    bottom = "+" <> String.duplicate("-", c) <> "+" <> @newline

    allPieces = blockMap(powerups) ++ frozen

    board = fillBoard(allPieces, board) |> Enum.reverse() |>
            List.insert_at(-1, bottom)

    first = List.first(board)
    first = String.trim(first) <> " #{num} pieces" <> @newline

    List.replace_at(board, 0, first) |> List.to_string()
  end
end
