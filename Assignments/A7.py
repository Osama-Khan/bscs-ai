# Write GPS operators in Python Syntax (marks will be deducted if Python syntax is violated),
# which could describe how the given final state can be achieved by the given initial state.
# Some constraints also apply; like only one disk can be moved at one time and disks can be
# removed from pole only from top, but can be placed anywhere on the table.

disk_ops = [
    {
        "action": "move green disk on table",
        "preconds": ["green disk on top", "red disk on pole"],
        "add":["blue disk on top", "green disk on table"],
        "delete":["green disk on top", "green disk on pole"]
    },
    {
        "action": "move blue disk on table",
        "preconds": ["blue disk on top", "red disk on pole"],
        "add":["red disk on top", "blue disk on table"],
        "delete":["blue disk on top", "blue disk on pole"]
    },
    {
        "action": "move red disk on table",
        "preconds": ["red disk on top"],
        "add":["red disk on table"],
        "delete":["red disk on top", "red disk on pole"]
    },
    {
        "action": "move green disk on pole",
        "preconds": ["red disk on table", "blue disk on table", "green disk on table"],
        "add":["green disk on pole", "green disk on top"],
        "delete":["green disk on table"]
    },
    {
        "action": "move blue disk on pole",
        "preconds": ["red disk on table", "blue disk on table", "green disk on pole"],
        "add":["blue disk on pole", "blue disk on top"],
        "delete":["blue disk on table", "green disk on top"]
    },
    {
        "action": "move red disk on pole",
        "preconds": ["red disk on table", "blue disk on pole", "green disk on pole"],
        "add":["red disk on pole", "red disk on top"],
        "delete":["red disk on table", "blue disk on top"]
    }
]

gps(["red disk on pole", "blue disk on pole", "green disk on pole",
     "green disk on top"],
    ["green disk on pole", "blue disk on pole", "red disk on pole",
     "red disk on top"],
    disk_ops)

# Tracing
#   0 Achieving: Green disk on pole
#   0 Consider: Move green disk on pole
#   1 Achieving: Red disk on table
#   1 Consider: Move red disk on table
#   2 Achieving: Red disk on top
#   2 Consider: Move blue disk on table
#   3 Achieving: Blue disk on top
#   3 Consider: Move Green disk on table
#   4 Achieving: Green disk on table
#   4 Achieved: Green disk on table
#   4 Achieving: Red disk on pole
#   4 Achieved: Red disk on pole
#   4 Action: Move Green disk on table
#   3 Achieving: Red disk on pole
#   3 Achieved: Red disk on pole
#   3 Action: Move Blue disk on table
#   2 Achieved: Red disk on top
#   1 Action: Move red disk on table
#   0 Action: Move green disk on pole
#   0 Achieving: Blue disk on pole
#   0 Action: Move blue disk on pole
#   0 Achieving: Red disk on pole
#   0 Action: move red disk on pole
#   0 Achieving: Red disk on top
#   0 Achieved: Red disk on top
#   Executing Move green disk on table
#   Executing Move blue disk on table
#   Executing Move red disk on table
#   Executing Move green disk on pole
#   Executing Move blue disk on pole
#   Executing Move red disk on pole
