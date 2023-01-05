# 1) Don't use loops at all
numbers = [10, 20, 33, 40, 50, 60, 70, 80]
result = 0
for num in numbers:
    result += num
    
print(result)

########### use this #############
result = sum(numbers)
print(result)

# 2) Use enumerate 
for idx in range(len(numbers)):
    print(idx, numbers[idx])
    
########### use this #############
numbers = [10, 20, 33, 40]
for idx, val in enumerate(numbers):
    print(idx, val)

########### try this #############
numbers = [10, 20, 33, 40]
for idx, val in enumerate(numbers, start=1):
    print(idx, val)
    
# 3) Use zip 
a = [1, 2, 3]
b = ["a", "b", "c"]

for idx in range(len(a)):
    print(a[idx], b[idx])
    
########### use this #############
a = [1, 2, 3, 4]
b = ["a", "b", "c"]

for val1, val2 in zip(a, b):
    print(val1, val2)
    
########### try this #############
a = [1, 2, 3, 4]
b = ["a", "b", "c"]

for val1, val2 in zip(a, b, strict=True):
    print(val1, val2)
    
# 4) Think lazy! Use a generator
events = [("learn", 5), ("learn", 10), ("relaxed", 20)]
minutes_studied = 0
for event in events:
    if event[0] == "learn":
        minutes_studied += event[1]
print(minutes_studied)

########### use this #############
study_times = (event[1] for event in events if event[0] == "learn")
minutes_studied = sum(study_times)
print(minutes_studied)

# 5.1) Use itertools!
lines = ["line1", "line2", "line3", "line4", "line5",
         "line6", "line7", "line8", "line9", "line10"]

for i, line in enumerate(lines):
    if i >= 5 :
        break
    print(line)
    
########### use this #############
from itertools import islice

first_five_lines = islice(lines, 5)
for line in first_five_lines:
    print(line)
    
########### try this #############
from itertools import islice

first_five_lines = islice(lines, 1, 5, 2)
for line in first_five_lines:
    print(line)
    
# 5.2) Use itertools!   
data = 'ABCDEFG'
for i in range(len(data)-1):
    print(data[i], data[i+1])

########### use this #############
from itertools import pairwise

for pair in pairwise('ABCDEFG'):
    print(pair[0], pair[1])
    
# 5.3) Use itertools!
for item in [1,2,4,-1,4,1]:
    if item >= 0:
        print(item)
    else:
        break
    
########### use this #############
from itertools import takewhile
items = takewhile(lambda x:x >= 0, [1,2,4,-1,4,1])
for item in items:
    print(item)
    
# 6.1) Use numpy 
import numpy as np

vec_a = [1, 2, 3]
vec_b = [4, 5, 6]

result = 0
for val1, val2 in zip(vec_a, vec_b):
    result += val1 * val2
print(result)

result = np.dot(vec_a, vec_b)
print(result)

# 6.2) Use numpy 
N = 100_000_000
def sum_python():
    return sum(range(N))

def sum_numpy():
    return np.sum(np.arange(N))

print(sum_python())
print(sum_numpy())

import timeit
print("sum python:", timeit.timeit(sum_python, number=1))
print("sum python:", timeit.timeit(sum_numpy, number=1))