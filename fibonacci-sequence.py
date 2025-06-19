def fibonacci_aux(num, sequence):
    if num == 1:
        sequence.append(1)
        return sequence

    if num == 2:
        sequence.append(1)
        return sequence

    next_value = sequence[-1] + sequence[-2]
    sequence.append(next_value)   

def fibonacci(num):
    sequence = []
    
    for i in range (1, num + 1):
        fibonacci_aux(i, sequence)
    
    return sequence

num = 5
fib = fibonacci(num)
print(f"Fibonnaci of {num} = {fib}")
