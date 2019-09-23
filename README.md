# Fetch Decode Execute

## Description
<p> For my CISC 433 (Elements of Computing) class I was given the task of simulating the Fetch, Decode, Execute Cycle. To accomplish this task I choose to use version 3.6 of the Python Prgramming language. </p>


## Data Structures and Constructs

### Ram(Primary Memory)
<p>The primary memory is emulated using a python List of Lists</p>

```
memory = [
    [0, 0, 1, 0, 0, 1, 1, 0],  # Load Memory Location (6)
    [0, 1, 1, 0, 0, 1, 1, 1],  # Add Memory Location (7)
    [0, 1, 0, 0, 0, 1, 1, 0],  # Store New Number in Location (6)
    [1, 0, 0, 0, 0, 0, 0, 0],  # Jump to location (0)
    # End of Instructions
    # Begin Value Address Space
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],  # Used to Store Big Number being computed
    [0, 0, 0, 0, 0, 1, 0, 1],  # Memory Location (7) Used to Store Number being Added (5)
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
```


## Architectural Overview

### Fetch:

### Decode:

### Execute:



## Conclusions


