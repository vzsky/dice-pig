from roller import Roller
from controller import Controller

if __name__ == "__main__" : 
  # 5 rolls then keep
  weight_5 = [0, -0.2, 0.95]
  roller_5 = Roller(weight_5)
  controller_5 = Controller(100, roller_5)
  print(controller_5.get_average_score(10000))

  # 20 points then keep
  weight_20 = [-0.3, 0, 0.95]
  roller_20 = Roller(weight_20)
  controller_20 = Controller(100, roller_20)
  print(controller_20.get_average_score(10000))

  #custom one
  weight_1 = [-0.72901638, -0.12570508, 3.5274755]
  roller_1 = Roller(weight_1)
  controller_1 = Controller(100, roller_1)
  print(controller_1.get_average_score(10000))

  weight_2 = [0.02373627, -0.52591227, 3.17936411]
  roller_2 = Roller(weight_2)
  controller_2 = Controller(100, roller_2)
  print(controller_2.get_average_score(10000))