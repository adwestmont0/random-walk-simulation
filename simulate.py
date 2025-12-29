
import matplotlib.pyplot as plt
import random
import statistics
import sys

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

    
class Experiment(object):
    def __init__(self):
        self.mean = 0.0
        self.stddeviation = 0.0
        self.variance = 0.0
        self.max_distance = 0
        self.trialcount = 0
        self.data = []

    def trial(self):
        self.trialcount = random.randint(500, 1000)
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
        plt.clf()
        plt.plot(self.data)
        plt.title("1D Random Walk (100 Steps, 1000 steps, 10000 steps)")
        plt.xlabel("Trial number")
        plt.ylabel("Final position")
        plt.savefig("plot.png")
        plt.show()
        plt.clf()
        plt.hist(self.data, bins=6)
        plt.title("Histogram - 1D Random Walk (100 Steps, 1000 steps, 10000 steps)")
        plt.xlabel("Final position value")
        plt.ylabel("Frequency")
        plt.savefig("plothist.png")
        plt.show()
            

def main():
    a = Experiment()
    a.trial()
    print(f"After {a.trialcount} trials")
    print(f"Mean position {a.mean}, Max distance (absolute) {a.max_distance}, standard deviation = {a.stddeviation}, variance = {a.variance}")
    a.plot()


if __name__ == '__main__':
    main()