defmodule Block do
  @moduledoc """
  This module contains method to create and manipulate a tetris block
  """
  import Dice

  @doc """
  createBlock(type, orientation) creates the initial block
  parameters:
    type - which tetris block to createBoard
    orientation - it's initial rotated state
  return: a list of maps containing information on a block (i.e.: x, y, l)
  """
  def createBlock(type, orientation) do
    case type do
      1 -> ["y",{0,0},{1,0},{0,1},{1,1}]
      2 -> ["r",{0,0},{1,0},{0,1},{-1,1}]
      3 -> ["g",{0,0},{-1,0},{0,1},{1,1}]
      4 -> ["b",{0,0},{-1,0},{1,0},{-1,1}]
      5 -> ["o",{0,0},{-1,0},{1,0},{1,1}]
      6 -> ["p",{0,0},{-1,0},{1,0},{0,1}]
      7 -> ["c",{0,0},{-1,0},{1,0},{2,0}]
    end |> blockMap() |> rotate("R", orientation)
  end

  @doc """
  blockMap([letter|pixels]) converts a tuple list to a list of maps
  parameters:
    letter: the character representing a blockMap
    pixels: a list of tuples
  return: a list of maps containing information on a block (i.e.: x, y, l)
  """
  def blockMap([letter|pixels]) do
    Enum.map(pixels, fn(pixel) ->
      %{l: letter, x: elem(pixel,0), y: elem(pixel,1)} end)
  end

  @doc """
  spawnBlock([pivot|rest], {c,r}) updates pivot's coordinates according to
                                  the given board dimensions
  parameters:
    pivot - the pivot point as a map of a block
    rest - the remaining pieces of a block
    c - the number of columns of the board
    r - the number of rows of the board
  return: a list of maps with pivot modified
  """
  def spawnBlock([pivot|rest], {c,r}) do
    midpoint = Integer.floor_div(c, 2)
    midpoint = Float.ceil(c/2) |> trunc()
    offset = Enum.max_by(rest, fn(pixel) -> pixel.y end).y

    pivot = Map.update!(pivot, :x, &(&1 = midpoint - 1))
    pivot = Map.update!(pivot, :y, &(&1 = r - 1 - offset))

    [pivot|rest]
  end

  @doc """
  setupBlock(dice, {c,r}) determines and creates a tetris block
  parameters:
    dice - a list of numbers
    c - the number of columns of the board
    r - the number of rows of the board
  return: a list containing the modified dice and a new block
  """
  def setupBlock(dice, {c,r}) do
    t = (dice = diceRoll(dice)) |> List.last()
    o = (dice = diceRoll(dice)) |> List.last()

    block = createBlock(t, o) |> spawnBlock({c,r})
    [dice, block]
  end

  @doc """
  getBlock([pivot|rest]) modifies a block with its actual coordinates
                         on the board
  parameters:
    pivot - pivot point, of type Map, of a block
    rest - other pieces in a block
  return: a new list of maps (the block)
  """
  def getBlock([pivot|rest]) do
    offsetX = pivot.x
    offsetY = pivot.y

    rest = Enum.map(rest, fn(pixel) ->
      %{l: pixel.l,
        x: pixel.x + offsetX,
        y: pixel.y + offsetY}
      end)

    [pivot|rest]
  end

  @doc """
  toList(listMap) converts a Map list to a list of tuples with only
                  coordinates (removes the letter)
  parameters:
    listMap - a list of maps
  return: a list of tuples
  """
  def toList(listMap) do
    Enum.reduce(listMap, [], fn(pt, acc) -> acc ++ [{pt.x, pt.y}] end)
  end

  @doc """
  rotate(rotated, _, 1) the base case. Rotates a given block
  parameters:
    rotated - a modified block (list of Maps)
  return: a modified block (list of Maps)
  """
  def rotate(rotated, _, 1) do
    rotated
  end

  @doc """
  rotate([pivot|rest], o, num) rotates a block
  parameters:
    pivot - pivot point, of type Map, of a block
    rest - other pieces in a block
    o - rotation direction
    num - number of rotations to perform
  return: a modified block (list of Maps)
  """
  def rotate([pivot|rest], o, num) do
    # convert each point ynegated @ x(right) or y @ xnegated
    unless (pivot.l == "y") do
      case o do
        "L" -> Enum.map(rest, fn(pixel) -> %{l: pixel.l,
               x: pixel.y * -1,
               y: pixel.x}
             end)
        "R" -> Enum.map(rest, fn(pixel) -> %{l: pixel.l,
               x: pixel.y,
               y: pixel.x * -1}
              end)
      end |> List.insert_at(0, pivot) |>
      rotate(o, num - 1)
    else
      [pivot|rest]
    end
  end

  @doc """
  translate([pivot|rest], offset) translates a given block
  parameters:
    pivot - pivot point, of type Map, of a block
    rest - other pieces in a block
    offset - number of cols to translate
  return: a modified block (list of Maps)
  """
  def translate([pivot|rest], offset) do
    pivot = Map.update!(pivot, :x, &(&1 + offset))
    [pivot|rest]
  end

  @doc """
  down([pivot|rest], offset) moves down a given block
  parameters:
    pivot - pivot point, of type Map, of a block
    rest - other pieces in a block
    offset - number of rows to move down
  return: a modified block (list of Maps)
  """
  def down([pivot|rest], offset) do
    pivot = Map.update!(pivot, :y, &(&1 - offset))
    [pivot|rest]
  end

end
