# dice pig

## rules

- player alternate turn
- in each turn, player roll a dice for as many times as they want
  - the score they gain in their turn is the sum of the results of rolls
  - the player may choose to end their turn anytime they wish
  - if the player roll a one, then they lose all the scores they have gained in that turn, and the turn ends
- which ever player reaches the score of {target} wins

## simplification

To simplify this game for an optimal strategy, it is reduced into a single player game.
The goal of the game is then to use smallest number of turn in the average scenario.
This strategy should works for both player, ignoring the fact that the first player have an advantage of one turn.
The action each player can choose to do is either to roll a dice, or to end the turn.

## basic strategy

There are two basic strategies for this game, which are, - Roll n dices and end the turn - Roll until the score reaches x and end the turn.

    The optimal values for n and x are determined mathematically to be n=5 and x=20.

## combined strategy

It is observed that the two strategies use different measure, which are the number of rolls and the accumulated score. Moreover, both strategies are optimal within its own group.
However, the optimal point when combining two measures might be better.

The easiest(?) representation of a decision making strategy is using a vector. The strategies are consider as a vector of size 3.
The input each strategy needs are (now) limited to only the number of rolls and the accumulated score. The biased term is also added, and will always be 1.
The input, a vector of size 3 and the strategy, a vector of size 3, will determine the decision. The decision is either 0, for ending the turn, or 1, for rolling the dice.
The decision is found as the dot product of the input and the strategy. The dot product is then mapped to a binary using step function, 0 if the value is negative, and 1 otherwise.

## genetic algorithm

Firstly, class of perceptron is created, as in roller. However, the perceptron will not be trained. There are no designated training for the perceptrons. Perceptrons, instead, undergoes evolution and mutation. Perceptrons have new gene over generation, and therefore be better at the given tasks.

However, in this state, the genetic algorithm is not very smart. There are only a few genes in consideration. In the step of breeding two perceptron, the most fit perceptrons will be chosen, and the breeding occurs randomly among them.

# barriers

Determining the fitness of perceptron takes a lot of time, even with caching.

## conclusion

the result is not very satisfying, the optimal strategy yeilded from the genetic algorithm performs, on average, the same as the basic strategy.