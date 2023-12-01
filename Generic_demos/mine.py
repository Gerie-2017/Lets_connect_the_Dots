def compute_ints(a=None,b=None):
    if a is None:
        a = int(input("Enter a number: "))
    if b is None:
        b = int(input("Enter another number: "))

    operator = input("Enter an operator: type among (+, -, *, /, %, **):")

    try:
        if b==0 and operator in ("/", "%"):
            print("Error: Cannot divide by zero.")
            return None
    except ValueError:
        print("Error: I cannot accept a zero value for the second number.")
        return None

    if operator == "+":
        result = (a+b)
    elif operator == "-":
        result= (a-b)
    elif operator == "*":
        result=(a*b)
    elif operator == "/":
        result=(a/b)
    elif operator == "%":
        result=(a%b)
    elif operator == "**":
        result=(a**b)
    else:
        print("Error: Invalid operator.")
        return None
    return result
result = compute_ints()
print(result)