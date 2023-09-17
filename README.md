# Simulate the infection in a computer network

## Overview

This project aims to simulate the spread of a virus in a network of computers using the Monte Carlo method. Originating from a problem described in exercise #5.10 of a textbook, the simulation incorporates randomness to accurately represent the infection phenomenon.

Through various user-configurable inputs, this simulation offers the ability to understand the behavior of virus spread in different conditions, making it a flexible and versatile tool.

## Features
Provides default values for quick simulations.
User input is facilitated for the number of computers, infection probability, computers repaired daily, and iterations.
Advanced Monte Carlo simulations for comprehensive results.
Visual representation through histograms to showcase the spread dynamics.
## Requirements
Python
Matplotlib for visual representation: pip install matplotlib
Any dependencies mentioned in distributions (Note: As distributions is not provided, ensure you have relevant imports and dependencies.)


## Usage

### Default Run

For a quick run with default parameters:
    
    python main.py

Algorithm diagram:

![project diagram](https://user-images.githubusercontent.com/67343196/174631088-3ade4371-8d14-4633-b3f2-6beafbaae054.png)

### User Input

You can configure:
- Number of computers in the network.
- Percentage of computers initially infected.
- Number of computers repaired daily.
- Number of iterations to simulate.
To use the simulation with user-defined values, you can just follow the on-screen prompts after starting the script.

## Results & Insights

The outcome of each simulation run gives:

- Average day required to fix all computers.
- Probability of each computer getting infected at least once.
- Expected number of computers infected daily.
The results can be used for deeper analysis, helping in designing strategies to prevent or control virus spread in real-world scenarios.

## Contribution & Development

Pull requests and contributions are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.

## Disclaimer

This is a simulation tool and is meant for educational purposes. The results should be used as a guide and not a definitive answer for real-world scenarios.





