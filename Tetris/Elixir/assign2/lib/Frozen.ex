defmodule Frozen do
  @moduledoc """
  This module is responsible for handling blocks which become frozen
  """

  @doc """
  addBlock([], frozen) Base case. adds a frozen block into a collection
  parameters:
    frozen - a list of maps (pieces of blocks that are frozen)
  return: a modified list of maps
  """
  def addBlock([], frozen) do
    frozen
  end

  @doc """
  addBlock([pixel|rest], [count|frozen]) adds a frozen block into a collection
  parameters:
    pixel - an individual piece of a block
    rest - the rest of the pieces of a block
    count - a list containing the number of pieces at each row
    frozen - a list of maps (pieces of blocks that are frozen)
  return: a modified list of maps
  """
  def addBlock([pixel|rest], [count|frozen]) do
    count = List.update_at(count, pixel.y, &(&1 + 1))
    frozen = frozen ++ [pixel]
    addBlock(rest, [count|frozen])
  end


  @doc """
  clearLine(0, frozen, _, _) Base case. Finds and removes frozen pieces in
                             completely filled rows
  parameters:
    frozen - a list of maps (pieces of blocks that are frozen)
  return: a modified list of (count, maps)
  """
  def clearLine(0, frozen, _, _) do
    frozen
  end

  @doc """
  clearLine(_, [count|frozen], c, :full) finds and removes frozen pieces in
                                     completely filled rows
  parameters:
    count - a list containing the number of pieces at each row
    frozen - a list of maps (pieces of blocks that are frozen)
    c - the number of columns of the tetris board
    :full - an Atom for pattern matching
  return: a modified list of (count, maps)
  """
  def clearLine(_, [count|frozen], c, :full) do
      i = Enum.find_index(count, fn(x) -> x == c end)
      if (i != nil) do
        frozen = Enum.filter(frozen, fn(pixel) -> pixel.y != i end)
        count = List.update_at(count, i, &(&1 * 0))
        clearLine(1, shift([count|frozen], i), c, :full)
      else
        clearLine(0, [count|frozen], c, :full)
      end
  end

  @doc """
  clearLine(num, [count|frozen], c, :powerClear) finds and removes frozen pieces in
                                             rows with only 1 empty cell
  parameters:
    num - number of recursive iterations
    count - a list containing the number of pieces at each row
    frozen - a list of maps (pieces of blocks that are frozen)
    c - the number of columns of the tetris board
    :powerClear - an Atom for pattern matching
  return: a modified list of (count, maps)
  """
  def clearLine(num, [count|frozen], c, :powerClear) do
    i = Enum.find_index(count, fn(x) -> x == (c - 1) end)
    if (i != nil) do
      frozen = Enum.filter(frozen, fn(pixel) -> pixel.y != i end)
      count = List.update_at(count, i, &(&1 * 0))
      clearLine(num - 1, shift([count|frozen], i), c, :powerClear)
    else
      clearLine(num - 1, [count|frozen], c, :powerClear)
    end
  end

  @doc """
  shift([count|frozen], i) resets the count at a specific row and
                       shifts all blocks in frozen greater than the row
                       previously cleared
  parameters:
  count - a list containing the number of pieces at each row
  frozen - a list of maps (pieces of blocks that are frozen)
  i - the row index
  return: a list of (count, maps)
  """
  def shift([count|frozen], i) do
    count = List.delete_at(count, i) |> List.insert_at(-1, 0)
    frozen = Enum.map(frozen, fn(pixel) ->
      if (pixel.y > i) do
        Map.update!(pixel, :y, &(&1 - 1))
      else
        pixel
      end
    end)
    [count|frozen]
  end

end
