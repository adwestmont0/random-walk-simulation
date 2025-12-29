
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
    print(f"After {a.trialcount} trials")
    print(f"Mean position {a.mean}, Max distance (absolute) {a.max_distance}, standard deviation = {a.stddeviation}, variance = {a.variance}")
    a.plot()


if __name__ == '__main__':
    main()