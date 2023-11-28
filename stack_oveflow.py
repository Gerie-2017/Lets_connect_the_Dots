# Stack overflow example with recursion
def recursive_function(count):
    print(f"Count: {count}")
    recursive_function(count + 1)

recursive_function(1)