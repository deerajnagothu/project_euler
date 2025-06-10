
def multiples(n):
    """
    Returns a list of all multiples of 3 or 5 below n.
    
    :param n: The upper limit (exclusive) for finding multiples.
    :return: A list of multiples of 3 or 5 below n.
    """
    nums = []
    for i in range(n):
        if i % 3 ==0 or i % 5 == 0:
            nums.append(i)
    return nums

def sum_of_multiples(n): 

    """
    Returns the sum of all multiples of 3 or 5 below n. 
    """
    return sum(multiples(n))
def main():
    """
    Main function to execute the problem solution.
    """
    n = 1000
    result = sum_of_multiples(n)
    # Execution time can be measured using time module if needed
    import time
    start_time = time.time()
    result = sum_of_multiples(n)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print(f"The sum of all multiples of 3 or 5 below {n} is: {result}")
if __name__ == "__main__":
    main()