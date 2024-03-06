def is_fibonacci_number(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False


test_numbers = [144, 15, 21, 50, 200, 987]
for n in test_numbers:
    if is_fibonacci_number(n):
        print(f"O numero: {n} pertence a sequência Fibonacci")
    else:
        print(f"O numero: {n} não pertence a sequência Fibonacci")
