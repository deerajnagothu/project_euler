
def fibonacci_type2(n): #less space with just two variables
    fib1 = 1
    fib2 = 2
    even_fib_sum = 0
    while fib1 < n:
        if fib1%2==0:
            even_fib_sum = even_fib_sum + fib1
        fib1,fib2=fib2,fib1+fib2
    return even_fib_sum

def fibonacci_type1(n): #redundant list space used
    fib_series = [1,2]
    even_fibs = [2]
    next = fib_series[0]
    while next < n:
        next = fib_series[-1] + fib_series[-2]
        if next < n:
            fib_series.append(next)
            if next%2==0:
                even_fibs.append(next)
    return sum(even_fibs)

def main():
    even_fib_sum = fibonacci_type2(4000000)
    print("Sum of even fibs ",str(even_fib_sum))
if __name__ == "__main__":
    main()
