def add_num(*args):
    """
    Sum of Integers
    """
    return sum(args)
list1 = list(map(int, input("Enter the numbers separated by spaces: ").split()))
print("sum =", add_num(*list1))
