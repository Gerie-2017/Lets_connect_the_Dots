def compute_ints(a=None,b=None):
    a = input("Enter a number: ", int(a))

    b = input("Enter another number: ", int(b))

    operator = input("Enter an operator: type among +, -, *, /, %, **:")

    try:
        if b==0: 
            print("Error: I cannot accept a zero value for the second number.")
    except ValueError:
        print("Error: I cannot accept a zero value for the second number.")

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
    return result
