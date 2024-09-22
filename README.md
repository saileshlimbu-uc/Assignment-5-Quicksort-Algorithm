Quicksort Algorithm: Implementation, Analysis, and Randomization
Overview
This repository contains the implementation of both the deterministic and randomized versions of the Quicksort algorithm. It includes performance analysis and an empirical comparison of their behavior on different types of input arrays.

The purpose of this project is to explore the Quicksort algorithm in detail, including its theoretical time complexity, the impact of randomization, and how different input data distributions affect performance.

Contents
deterministic_quicksort.py: Python implementation of the deterministic version of Quicksort.
randomized_quicksort.py: Python implementation of the randomized version of Quicksort.
performance_analysis.py: Script to compare the running times of both versions on various input types (random, sorted, reverse-sorted arrays).
report.pdf: A detailed report discussing the implementation, analysis, and results.
README.md: Instructions on how to run the code and an overview of the repository.
Setup and Requirements
To run the code in this repository, you will need:

Python 3.x installed on your system.
The random and time libraries are used in the scripts (they are part of Python’s standard library).
You can install Python from the official Python website.

Running the Code
1. Deterministic Quicksort
To run the deterministic version of Quicksort:

bash
Copy code
python deterministic_quicksort.py
2. Randomized Quicksort
To run the randomized version of Quicksort:

bash
Copy code
python randomized_quicksort.py
3. Performance Analysis
The performance_analysis.py script allows you to compare the execution times of both versions of Quicksort on random, sorted, and reverse-sorted arrays of various sizes.

To run the performance analysis:

bash
Copy code
python performance_analysis.py
This will output the time taken by each version of Quicksort for different input arrays.

Summary of Results
The deterministic version of Quicksort performs poorly on sorted and reverse-sorted arrays, leading to 
𝑂
(
𝑛
2
)
O(n 
2
 ) performance in the worst-case.
The randomized version of Quicksort consistently performs better due to reduced likelihood of encountering the worst-case scenario.
The randomized pivot selection proves to be an effective method for improving the performance of Quicksort on various input distributions.
