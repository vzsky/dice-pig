from controller import Controller
from roller import Roller
import numpy as np
import random

population_size = 100
total_generations = 20
total_parents = 30
chromosome_size = 5
mutation_prob = 0.05
mutation_strength = 0.1
target = 100
gene_max = 1.0
fitness_trial = 10000

class Organism :
  def __init__ (self, target, weight) :
    self.roller = Roller(weight)
    self.controller = Controller(target, self.roller)
    self.cache_fitness = 0

  @property
  def fitness (self) : 
    if self.cache_fitness != 0 : 
      return self.cache_fitness
    self.cache_fitness = self.controller.get_average_score(fitness_trial)
    return self.cache_fitness


if __name__ == "__main__" : 

  population_gene = np.random.uniform(low=-gene_max, high=gene_max, size=(population_size, chromosome_size))
  population = [Organism(target, member) for member in population_gene]
  population = sorted(population, key=lambda o:o.fitness)

  for turn in range(total_generations) : 

    print("generation", turn)

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
        child_weight[index] = (1-mutation_strength)*child_weight[index] + mutation_strength*np.random.uniform(low=-gene_max, high=gene_max)

      child = Organism(target, child_weight)  
      offsprings.append(child)

    population = offsprings + parents
    population = sorted(population, key=lambda o:o.fitness)

    print(population[0].controller.roller.weight)
    print(population[0].fitness)
    print("real measure", population[0].controller.get_average_score(10000))