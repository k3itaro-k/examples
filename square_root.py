'''Square root(positive)

execution_time takes a function as a argument and prints information 
about its execution time.

aproximate_time  takes two arguments: target and epsilon(0.01 by default) and returns
the square root of a given integer(target).

binary_search_root takes two arguments: target and epslion(0.01 by default) and returns
the square root of a given integer(target).

'''

import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = time.time()
        func(*args, **kwargs)
        final_time = time.time()
        elapsed_time = final_time - initial_time
        print(f'The function {func.__name__} finish its calculation in {elapsed_time} seconds')
    return wrapper

@execution_time
def aproximate_solution(target: int, epsilon: float = 0.01) -> None:    
    step = epsilon ** 2
    answer = 0.0 

    while abs(answer ** 2 - target) >= epsilon and answer <= target:
        answer += step

    print(f'The square root of {target} with an epsilon of {epsilon} is {answer}') 

@execution_time
def binary_search_root(target: int, epsilon: float = 0.01) -> None:
    low = 0.0
    high = max(1.0, target)
    answer = (high + low) / 2

    while abs(answer ** 2 - target) >= epsilon:

        if answer ** 2 < target:
            low = answer
        else:
            high = answer
        
        answer = (high + low) / 2
    
    print(f'The square root of {target} with an epsilon of {epsilon} is {answer}')

def main():
    print('This program calculates the square root of a given number using two differents methods.')
    try:
        target = int(input('Please, give a integer :'))
    except ValueError as e:
        print('Error: The given value is not integer.')
        return None
    binary_search_root(target)
    aproximate_solution(target)

if __name__=='__main__':
    main()
