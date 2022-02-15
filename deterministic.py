from roller import Roller
from controller import Controller

def get_result_from_strategy (strategy, target = 100, avg_from = 10000) :
  roller = Roller(strategy)
  controller = Controller(target, roller)
  print(controller.get_average_score(avg_from))

if __name__ == "__main__" : 
  # 5 rolls then keep
  get_result_from_strategy([0, -0.2, 0, 0, 0.95])

  # 20 points then keep
  get_result_from_strategy([-0.05, 0, 0, 0, 0.95])

  # FROM GENETIC ALGORITHM
