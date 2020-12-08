# Write Python function named 'print-in-range' to input two numbers and choice
# (either even or odd) from user and display all even or odd numbers (based on
# choice) between the given range. The function must be a recursive function
# (NOT Iterative function). Note that the first given number can be greater
# than second number or it can be less than second number, in both cases series
# should be printed.

def print_in_range(n1, n2, choice):
    if n1 > n2:
        n1, n2 = n2, n1

    if choice == "even" and n1 % 2 == 0:
        print(n1)
    elif choice == "odd" and n1 % 2 != 0:
        print(n1)
    if n1 == n2:
        return
    else:
        print_in_range(n1 + 1, n2, choice)


print_in_range(10, 5, "even")
