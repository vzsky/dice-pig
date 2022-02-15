import numpy as np

def to_binary (x) :
  return 1 if x > 0 else 0

class Roller :
  """2 dimension -- decide on rolling a dice"""
  def __init__ (self, weight) :
    self.weight = weight
  
  def action (self, input) :
    input.append(1)
    input = np.array(input)
    return to_binary(np.dot(input.T, self.weight))