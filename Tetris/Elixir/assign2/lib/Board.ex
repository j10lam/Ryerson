defmodule Board do
  @moduledoc """
  This module contains methods to create and populate a board
  """

  @newline "
"
  @doc """
  createBoard({c,r}) creates a list of String to simulate a tetris board
  parameters:
    c - number of columns
    r - number of rows
  return: a new list
  """
  def createBoard({c,r}) do
    aRow = "|" <> String.duplicate(" ", c) <> "|" <> @newline
    List.duplicate(aRow, r)
  end

  @doc """
  fillBoard([], board) is the base case method of fillBoard
  parameters:
    [] - an empty list
    board - a list containing the rows of a tetris board
  return: board
  """
  def fillBoard([], board) do
    board
  end

  @doc """
  fillBoard([p|tail], board) replaces elements in the list, board
  parameters:
    p - a singular piece of a block
    tail - the remaining pieces of a block
    board - a list containing the rows of a tetris board
  return: a modified board
  """
  def fillBoard([p|tail], board) do
    aRow = Enum.at(board, p.y) |> String.split("", trim: true)
    aRow = List.replace_at(aRow, (p.x + 1), p.l) |> List.to_string()
    board = List.replace_at(board, p.y, aRow)

    fillBoard(tail, board)
  end

end
