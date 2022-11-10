from functools import reduce
from operator import mul

arr = [1, 0, 2, 3, 0, 4]
tmp = arr[arr.index(0) + 1:]
arr = tmp[: arr.index(0) + 1]
print(sum(arr), reduce(mul, arr), sep='\n')
