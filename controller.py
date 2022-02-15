from game import Game
class Controller :
  """2 dimension -- control interaction of during gameplay"""
  def __init__ (self, target, roller) :
    self.roller = roller
    self.game = Game(target)

  def _get_game_stat (self) :
    stat = []
    stat.append(float(self.game.accumulated_value)/6.0)
    stat.append(float(self.game.number_of_continuous_roll))
    return stat

  def _get_roller_action (self) : 
    stat = self._get_game_stat()
    return self.roller.action(stat)
  
  def play_game (self) : 
    action = self._get_roller_action()
    score = self.game.action(action)
    return score

  def get_score (self) : 
    score = 0
    while score == 0 : 
      score = self.play_game()
    self.game.reset()
    return score
  
  def get_average_score (self, times) : 
    s = 0.0
    for i in range(times) : 
      s += self.get_score()
    return s/times
