from math import sqrt
import copy
from euler import *
import datetime

def count_blocks(line_length, min_size, cache):
    solutions = 1
    if min_size > line_length:
        return solutions

    if line_length in cache:
        return cache[line_length]

    for start_pos in range(0, line_length - min_size + 1):
        for block_length in range(min_size, line_length - start_pos + 1):
            solutions += count_blocks(line_length - start_pos - block_length - 1, min_size, cache)

    if line_length not in cache:
        cache.update({line_length: solutions})
        print 'appended to cache', line_length, solutions

    return solutions

start = datetime.datetime.now()

cache = {}
print count_blocks(50, 3, cache)

print datetime.datetime.now() - start