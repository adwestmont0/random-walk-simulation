## Random Walk Simulation Using Python

# Overview

This project simulates one-dimensional random walks using Python and visualizes the results with matplotlib. Each random walk begins at position 0 and moves either +1 or −1 at each step with equal probability. By running many trials, the project explores how randomness behaves statistically over time.

# Motivation

I was curious how unpredictable individual random processes can still produce consistent mathematical patterns when analyzed across many trials. This project allowed me to combine probability, statistics, and programming to explore that idea computationally.

# What the Program Does

Simulates multiple one-dimensional random walks

* Tracks the position at each step for a sample walk

* Records final positions across many trials

* Computes statistical measures such as mean and standard deviation

* Visualizes results using line plots and histograms

* Saves plots as high-resolution PNG files

# Key Results

* Individual random walks vary significantly and appear unpredictable

* The mean final position across many trials remains close to zero due to symmetry

* The distribution of final positions spreads out as the number of steps increases

* This demonstrates fundamental probability concepts such as randomness, variance, and the law of large numbers

# Technologies Used

* Python 3

* matplotlib

* random

* statistics

# How to Run

1. Ensure Python 3 is installed

2. Install matplotlib (if not already installed)

pip install matplotlib


3. Run the simulation:

python simulate.py

# Output

<mark> random_walk.png </mark> — line plot of a sample random walk

<mark> final_positions_histogram.png </mark> — histogram of final positions across trials

# What I Learned

This project strengthened my understanding of probability, statistical analysis, and data visualization. It also showed me how computational simulations can be used to model and analyze mathematical systems that are difficult to study analytically.

# Future Extensions

I am planning to add support for 2D and higher dimensional random walks.