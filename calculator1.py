import sys

if len(sys.argv) == 4:
    try:
        first_param = int(sys.argv[1])
        operator = sys.argv[2]
        second_param = int(sys.argv[3])

        match operator:
            case "+":
                print(first_param + second_param)
            case "-":
                print(first_param - second_param)
            case "*" | "\\*":
                print(first_param * second_param)
            case "/":
                print(first_param / second_param)
            case "%":
                print(first_param % second_param)
            case "^":
                print(first_param**second_param)
            case _:
                print("input error")
    except:
        print("input error")

else:
    first_param = "usage: python3 ./solution.py a_number (an_operator +-*/%^) a_number"
    print(first_param)
