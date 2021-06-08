'''
Fibonacci generator.

This function generates n fibonacci's numbers.
'''


def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b , b+a


if __name__=='__main__':
    for i in fibonacci(10):
        print(i)        
