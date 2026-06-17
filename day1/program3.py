a=int(input("enter a value:"))
b=int(input("enter b value:"))
op=input("enter a operator")
match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "%":
        print(a%b)
    case "/":
        print(a/b)
    case "//":
        print(a//b)
    case "**":
        print(a**b)
    case "__":
        print("invalid operator")
