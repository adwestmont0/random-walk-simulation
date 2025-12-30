
'''
We imported these libraries to access its functions with the dot notation syntax 
'''

import matplotlib.pyplot as plt
import random
import statistics
import sys

'''
This class models a random 1D walk. It tracks the position with an initial value of 0.
It exposes a step and run method for callers. Each invocation of the step method increments
or decrements the position by one with an equal probability and the run method executes
this random choice for a series of 100, 1000, and 10000 steps.
'''
class RandomWalk1D(object):
    def __init__(self):
        self.position = 0


    def step(self):
        self.position += random.choice([-1, 1])
        

    def run(self):
        num_steps = [100, 1000, 10000]
        for _, steps in enumerate(num_steps):
            for i in range(steps):
                self.step()

    def runSteps(self, steps):
        for i in range(steps):
            self.step()

'''
This new class models an experiment that runs multiple trials of a 1D random walk.
It collects data from each trial and computes statistical measures such as mean, 
standard deviation, variance, and maximum distance from the origin. It also includes 
a method to plot the results using matplotlib
'''
    
class Experiment(object):
    def __init__(self, trialcount=None):
        self.mean = 0.0
        self.stddeviation = 0.0
        self.variance = 0.0
        self.max_distance = 0
        self.trialcount = trialcount
        self.data = []

    def trial(self):
        self.trialcount = random.randint(500, 1000) if self.trialcount is None else self.trialcount
        total = 0
        for i in range(self.trialcount):
            walk1D = RandomWalk1D()
            walk1D.run()
            self.data.append(walk1D.position)
            
        self.mean = statistics.mean(self.data)
        self.stddeviation = statistics.stdev(self.data)
        self.variance = statistics.variance(self.data)
        self.max_distance = abs(max(self.data, key=abs))

    def plot(self):
        plt.plot(self.data)
        plt.title("1D Random Walk (100 Steps, 1000 steps, 10000 steps)")
        plt.xlabel("Trial number")
        plt.ylabel("Final position")
        plt.axhline(self.mean, color='red', linestyle='--')
        plt.savefig("random_walk.png", dpi=300)
        plt.show()
        plt.close()
        plt.hist(self.data, bins=6)
        plt.title("Distribution of Final Positions After Random Walks")
        plt.xlabel("Final Position")
        plt.ylabel("Frequency")
        plt.axvline(self.mean, color='red', linestyle='--')
        plt.savefig("final_positions_histogram.png.png")
        plt.close()
       

def main():
    a = Experiment()
    a.trial()
    print(f"After {a.trialcount} trials, Mean Value {a.mean}, Max distance (absolute) {a.max_distance}, standard deviation = {a.stddeviation}, variance = {a.variance} ")
    a.plot()

if __name__ == '__main__':
    main()