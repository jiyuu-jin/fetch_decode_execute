# Fetch Decode Execute

## Description
<p> For my CISC 433 (Elements of Computing) class I was given the task of simulating the Fetch, Decode, Execute Cycle. To accomplish this task I choose to use version 3.6 of the Python Prgramming language. </p>


## Data Structures and Constructs

### Ram(Primary Memory)
<p>The primary memory is simulated using a python List of Lists. There are a total of ten memory address spaces and each space consists of 8 bits. The first three bits int he List is used for the instruction opcode with the following five bits used to store a given value.</p>

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

### Helper Functions

<p><b>to_binary:</b> The to_binary function is used to convert an 8 bit List of integers to a base two integer value. It works by looping throught the given List and conncatinating each Index value to a string. That string is then casted to a base two integer.</p>

```
def to_binary(value):
    return int("".join(str(x) for x in value), 2)

```

<p><b>get_from_ram:</b> The get_from_ram is used to simulate the native process of fetching address values from ram. It works by taking the current memory address register(mar. It passes the mar to the to_binary fucntion to  get an integer repersentation and then passes it into the memory List to retrive a given index location. This is wrapped in a try except that catches out of range indexs and Halts the System if it attempts to access an out of bounds memory location.</p>

```
def get_from_ram():
    try:
        location = to_binary(mar)
        return memory[location]
    except IndexError:
        print("\n", "Memory Address out of Range halting")
        halt = True
```


### Fetch:

### Decode:

### Execute:



## Conclusions


