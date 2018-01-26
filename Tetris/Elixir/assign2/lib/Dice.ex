defmodule Dice do
  @moduledoc """
  This module contains methods related to the dice
  """

  @doc """
  diceRoll([head|tail]) appends head to the end of tail
  parameters:
    head - the head of a given list
    tail -  the tail of a given list
  return: a list
  """
  def diceRoll([head|tail]) do
    tail ++ [head]
  end

end
