# Write GPS operators to achieve final state by moving blocks present in the sequence as shown 
# in initial state. Note that at one time only one block can be picked (and only from top).
# INIT      FINAL
# C         C
# B         B
# D  A      A  D

import sys
sys.path = ['..', 'algos']
from gps import gps

disk_ops = [
    {
        "action": "move c on table",
        "preconds": ["c on top", "a on table"],
        "add":["c on table", 'b on top'],
        "delete":["c on top", 'c on stack']
    },
    {
        "action": "move b on table",
        "preconds": ["b on top", "a on table"],
        "add":["b on table", "d on top"],
        "delete":["b on top", "b on stack"]
    },
    {
        "action": "move d on table",
        "preconds": ["d on top"],
        "add":["d on table"],
        "delete":["d on top", "d on stack"]
    },
    {
        "action": "move a on stack",
        "preconds": ["a on table", "d on table"],
        "add":["a on stack", "a on top"],
        "delete":["a on table"]
    },
    {
        "action": "move b on stack",
        "preconds": ["b on table", "a on stack"],
        "add":["b on top", "b on stack"],
        "delete":["b on table", "a on top"]
    },
    {
        "action": "move c on stack",
        "preconds": ["c on table", "a on stack"],
        "add":["c on top", "c on stack"],
        "delete":["c on table", "b on top"]
    }
]

initial = ["d on stack", 'b on stack', "c on top", "c on stack", "a on table"]
final = ["a on stack", 'b on stack', "c on top", "c on stack", "d on table"]
gps(initial, final, disk_ops)