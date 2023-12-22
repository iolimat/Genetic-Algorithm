import numpy as np
class GeneticBase:
    def __init__(self,type_crossover='single point',probability_crossover=0.7,max_population=1000,probability_mutation=0.3,population_size=100,num_of_generations=50):
        self._ctype=type_crossover
        self._cross=probability_crossover
        self._mutati=probability_mutation
        self._size=population_size
        self._num_gen=num_of_generations
        self._mpopulation=max_population

    def initialize_parameter():
        raise NotImplementedError
    def generate_random_solution():
        raise NotImplementedError
    def single(self,parent1,parent2):
        point=np.random.randint(0,self._ndim)
        o1=np.concatenate((parent1[:point],parent2[point:]))
        o2=np.concatenate((parent2[:point],parent1[point:]))
        return(o1,o2)
    def two(self,parent1,parent2):
        point1=np.random.randint(0,self._ndim)
        point2=np.random.randint(0,self._ndim)    
        if point1 > point2:
            point1, point2 = point2, point1
        elif point1 == point2:
            point2 += 1
        o1 = np.concatenate((parent1[:point1], parent2[point1:point2], parent1[point2:]))
        o2 = np.concatenate((parent2[:point1], parent1[point1:point2], parent2[point2:]))
        return(o1,o2)
    def _uniform(self,parent1,parent2):
        o1=o2=np.array([])
        for j in range(self._ndim):
            if np.random.random() < 0.5:
                o1=np.append(o1,parent2[j])
                o2=np.append(o2,parent1[j])
            else:
                o1=np.append(o1,parent1[j])
                o2=np.append(o2,parent2[j])
        return(o1,o2)
    def _crossover(self,parents):
        if parents.shape[0] % 2 == 1:
            parents = parents[:-1]
        offspring=np.array([])
        for i in range(0, len(parents)-1, 2):
            if self._ctype=='single point':
                o1,o2=self._single(parents[i],parents[i+1])
            elif self._ctype=='two point':
                o1,o2=self._two(parents[i],parents[i+1])
            elif self._ctype=='uniform':
                o1,o2=self._uniform(parents[i],parents[i+1])
            offspring=np.concatenate((o1,o2,offspring))
        return offspring
    def mutate():
        raise NotImplementedError
    def evaluate():
        raise NotImplementedError
    def filter():
        raise NotImplementedError
    def processing(self,solution,evaluation):
        cc=self._crossover(solution)
        solution=np.append(solution,cc).reshape(-1,self._ndim)
        if self._size>self._mpopulation:
            solution=self._filter(solution,evaluation)
        self.size=solution.shape[0]
        for i in range(self._size):
            if np.random.random() < self._mutati:
                solution[i]=self.mutate(solution[i]) 
        return solution
    def fit(self):
       raise NotImplementedError
class GeneticText(GeneticBase):
    def __init__(self,type_crossover='single point',probability_crossover=0.7,max_population=1000,probability_mutation=0.3,population_size=100,num_of_generations=50):
        super().__init__(type_crossover,probability_crossover,max_population,probability_mutation,population_size,num_of_generations)
    def initialize_parameter(self):
        self._target= np.array(list(input('Enter trager: ')))
        self._ndim=self._target.shape[0]
        self._gene=np.array(list('''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, .-;:_!"'#%&/()=?@${[]}'''))
    def generate_random_solution(self):
        return np.random.choice(self._gene,size=(self._size,self._ndim))
    def mutate(self,solution):
        mutation_point = np.random.randint(0,self._ndim)
        new_solution = np.copy(solution)
        new_solution[mutation_point]=np.random.choice(self._gene)
        return new_solution
    def evaluate(self,solution):
        return self._ndim-np.sum(self._target == solution,axis=1)
    def filter(self,solution,evaluation):
        evaluation=np.argsort(evaluation)[-int(self._size/2):]
        return solution[evaluation]
    def fit(self):
        self.initialize_parameter()
        solution=self.generate_random_solution()
        for _ in range(self._num_gen):
            evaluation=self.evaluate(solution)
            k=int(self._cross * self._size)
            solution=solution[np.argsort(evaluation)[:k]]
            if 0 in evaluation:
                break
            solution=self.processing(solution,evaluation)
            print(solution[0])
        return solution[0]

class GeneticNumber(GeneticBase):
    def __init__(self,type_crossover='single point',probability_crossover=0.7,max_population=1000,probability_mutation=0.3,population_size=100,num_of_generations=50,problem_type='maximize'):
        super().__init__(type_crossover,probability_crossover,max_population,probability_mutation,population_size,num_of_generations)
        self._p_type=problem_type
    def initialize_parameter(self):
        self._ndim=int(input('Enter number of dimintions: '))
        self._upper=float(input('Enter the upper bound of random solution: '))
        self._lower=float(input('Enter the lower bound of random solution: '))
    def generate_random_solution(self):
        return np.random.uniform(self._lower,self._upper, size=(self._size,self._ndim))
    def mutate(self,solution):
        mutation_point = np.random.randint(0,self._ndim)
        new_solution = np.copy(solution)
        mutation_value = np.random.uniform(self._lower,self._upper)
        new_solution[mutation_point] += mutation_value
        return new_solution
    def evaluate(self,solution):
        return [5*solution[i][0]+2.4*solution[i][1]+7.5*solution[i][2]+0.8*solution[i][3] for i in range(self._size)]
    def filter(self,solution,evaluation):
        if self._p_type=='maximize':
            evaluation=np.argsort(evaluation)[-int(self._size/2):]
        else:
            evaluation=np.argsort(evaluation)[:int(self._size/2)]
        return solution[evaluation]
    def fit(self):
        self.initialize_parameter()
        solution=self.generate_random_solution()
        for _ in range(self._num_gen):
            evaluation=self.evaluate(solution)
            k=int(self._cross * self._size)
            solution=solution[np.argsort(evaluation)[:k]]
            solution=self.processing(solution,evaluation)
        return solution[0]
if __name__=='__main__':
    GA=GeneticText(num_of_generations=40,probability_crossover=0.9,type_crossover='uniform',population_size=300)
    GA.fit()