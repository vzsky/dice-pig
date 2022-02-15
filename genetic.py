from controller import Controller
from roller import Roller
import numpy as np
import random

class Organism :
  def __init__ (self, target, weight) :
    self.roller = Roller(weight)
    self.controller = Controller(target, self.roller)

  @property
  def fitness (self) : 
    return self.controller.get_average_score(50)


if __name__ == "__main__" : 

  population_size = 1000
  total_generations = 20
  total_parents = 35
  chromosome_size = 3
  mutation_prob = 0.1

  population_gene = np.random.uniform(low=-4.0, high=4.0, size=(population_size, chromosome_size))
  population = [Organism(100, member) for member in population_gene]

  for turn in range(total_generations) : 

    print("generation", turn)

    population = sorted(population, key=lambda o:o.fitness)

    parents = population[0:total_parents]
    offsprings = []
    for i in range(population_size-total_parents) : 
      p1, p2 = random.sample(parents, k=2)
      split = random.randrange(1, chromosome_size)
      p1_weight = p1.controller.roller.weight
      p2_weight = p2.controller.roller.weight
      child_weight = np.concatenate((p1_weight[:split], p2_weight[split:]))

      if random.random() < mutation_prob : 
        index = random.randrange(0, chromosome_size)
        child_weight[index] = 0.5*child_weight[index] + 0.5*np.random.uniform(low=-4.0, high=4.0)

      child = Organism(100, child_weight)  
      offsprings.append(child)

    population = offsprings + parents

    population = sorted(population, key=lambda o:o.fitness)
    print(population[0].controller.roller.weight)
    print(population[0].controller.get_average_score(100))