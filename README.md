# Take-Home Assignment

## Overview
Implement a virtual memory manager that manages allocations and deallocations on a large contiguous block of memory.

## Project Requirements

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Instructions
1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
python pytest tests.py
```

## Decision Choices

### Pointers
- Python does not have raw pointers, so I implemented a data structure that represents the functionality of a pointer.
- Pointers are represented as `int` in this project for simplicity and performance.
- For free slots, the pointer is the first element of the tuple, while the second element represents the slot size.
- For allocated slots, the key represents the pointer and the value represents the slot size.

### Data Structure for Free Slots
- Free slots are stored in a list containing tuples.
- This data structure was chosen because it works well with the merge algorithm, which iterates through the list to find overlapping free slots.

### Data Structure for Allocated Slots
- Allocated slots are stored in a dictionary, with keys as pointers and values as the size of the allocated slot.
- Because we know exactly which pointer to remove from allocated slots, the dictionary is chosen for its fast, constant-time lookups.

## Algorithms
- I implement a first-fit algorithm such that the buffer is allocated starting from the first available slot.
- The merge algorithm is a simple approach that checks if free slots overlap and merges them if they are adjacent.

## Possible Optimisations
- To optimise allocations, I would implement a map to track fragmented available free slots so that I can look up slots of an exact size faster rather than looping through the entire list.
- For the merge algorithm, instead of sorting and iterating each time memory is freed, I may consider using a binary search (Python's bisect) to quickly locate overlapping slots. This approach would eliminate the need to sort the list every time the buffer is freed.

## Future Design Considerations
- As this project is relatively simple, I use an `int` to represent a pointer for simplicity and performance. However, for a more complex system, I might implement a dedicated pointer class.
- I considered implementing a min heap as a future design option to eliminate the need to sort the free_slots list every time a slot is freed. However, using a min heap may complicate the merging process, so it might be used in conjunction with another data structure to track slots.
- If given more time, the project structure could be improved by abstracting out the classes and functions instead of placing everything in a single file. This would aid in unit testing each function and result in cleaner, more maintainable code.

## Testing and Error Handling

### Edge Cases
- In the future, I will add more detailed tests to provide specific error messages, such as for full buffer scenarios and out-of-bound allocations.

## Assumptions
- To tackle fragmentation, I assume that adjacent free slots will be merged when a pointer is removed.