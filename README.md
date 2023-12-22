# Genetic Algorithm for Optimization

## Overview
This repo is to help you understand genetic algorithm it cant be used on real applications

This project provides a flexible and extensible implementation of a Genetic Algorithm (GA) for optimization tasks. The primary purpose of this framework is to find optimal solutions through evolution inspired by the principles of natural selection. The GA can of handling both text and numerical optimization problems.

## GeneticBase Class

The `GeneticBase` class serves as the foundation for the genetic algorithm. It encapsulates essential parameters and methods required for the optimization process. Key attributes include:

- `type_crossover`: Type of crossover operation (default: 'single point').
- `probability_crossover`: Probability of crossover occurring (default: 0.7).
- `max_population`: Maximum population size (default: 1000).
- `probability_mutation`: Probability of mutation occurring (default: 0.3).
- `population_size`: Initial population size (default: 100).
- `num_of_generations`: Number of generations for the evolutionary process (default: 50).

The `GeneticBase` class provides methods for initialization, solution generation, crossover, mutation, evaluation, and filtering.

## GeneticText Class

The `GeneticText` class inherits from `GeneticBase` and is tailored for text-based optimization problems. It includes methods for initializing parameters, generating random solutions, mutating solutions, evaluating fitness, and filtering the population. Example usage demonstrates how the GA can be applied to solve a text optimization problem, such as finding a target string.

## GeneticNumber Class

The `GeneticNumber` class, also inheriting from `GeneticBase`, is designed for numerical optimization problems. It incorporates methods for initializing parameters, generating random numerical solutions, mutating solutions, evaluating fitness, and filtering the population. The example usage showcases solving a numerical optimization problem.

## Example Usage

The provided example at the end of the script demonstrates how to instantiate and utilize the `GeneticText` class for a text-based optimization problem. Users can customize the GA parameters to suit their specific optimization needs.

Feel free to explore and adapt this framework for your optimization tasks. If you have any questions or need further assistance, please don't hesitate to reach out.
