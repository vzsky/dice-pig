import random

def dice () : 
  return random.randint(1, 6)

class Game :
  """regulate gameplay"""
  def __init__ (self, target) : 
    self.target = target
    self.accumulated_value = 0
    self.number_of_turn = 0
    self.number_of_continuous_roll = 0
    self.kept_value = 0

  def _roll (self) : 
    self.number_of_continuous_roll += 1
    result = dice()
    if (result == 1) :
      self.accumulated_value = 0
      self.number_of_continuous_roll = 0
      self.number_of_turn += 1
    else :
      self.accumulated_value += result

  def _keep (self) : 
    self.kept_value += self.accumulated_value
    self.number_of_continuous_roll = 0
    self.accumulated_value = 0
    self.number_of_turn += 1

  def action (self, mode) : 
    if mode == 1 : 
      self._roll()
    else :
      if self.accumulated_value == 0 : 
        return 999999
      self._keep()
    if self.accumulated_value + self.kept_value > self.target :
      return self.number_of_turn + 1
    return 0

  def reset (self) : 
    self.accumulated_value = 0
    self.number_of_turn = 0
    self.number_of_continuous_roll = 0
    self.kept_value = 0