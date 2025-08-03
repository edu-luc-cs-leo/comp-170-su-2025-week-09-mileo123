def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    """
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum. The last digit is always the remainder of
        # the integer division by base of the number system in use (here: 10).
        sum += n % 10 
        # Remove the last digit. This can be done by integer division of the number with
        # its number base (here: 10). For exampe 24 // 10 = 2 (and thus 4 is gone!)
        n //= 10
    # Done
    return sum + n

def count_occurrences_iterative(data_list, target):
    count = 0
    # Iterate over the input list
    for i in range(len(data_list)):
        # Check if current list item matches target value
        if data_list[i] == target:
            # If it does, increment the counter
            count += 1
    # Done
    return count


# WRITE YOUR CODE BELOW

def sum_of_digits(n):
  """Returns the sum of the digits of a number recursively"""
  if n < 10:
     return n # its a single digit so its a base case
  else:
       return (n % 10) + sum_of_digits(n // 10) # its a recursive case



def count_occurrences(data_list, target):
    """Returns how many times target appears in data_list using recursion."""
    if data_list == []:
        return 0  # case empty list
    else:
        if data_list[0] == target:
            return 1 + count_occurrences(data_list[1:], target)
        else:
            return count_occurrences(data_list[1:], target)


def factorial_iterative(n):
    """Returns n! using iteration."""
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def fibonacci_iterative(n):
    """Returns the nth Fibonacci number using iteration."""
    if n == 1:
        return 1
    if n == 2:
        return 2

    first = 1
    second = 2
    current = 0

    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return current

