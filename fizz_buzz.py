'''
FIZZ BUZZ

This function prints "fizz" if a number i is a multiple of 3, "buzz" if i is a multiple of 5 and 
"fizzbuzz" if i is a multiple of 3 and 5, otherwise prints i, the range of i starts in 1 and finish in 100.
'''

def fizzbuzz():
    for i in range(1,101):
        if i%5==0 and i%3==0:
            print('fizzbuzz')
        elif i%5==0:
            print('Buzz')
        elif i%3==0:
            print('Fizz')
        else:
            print(i)

if __name__=="__main__":
    fizzbuzz()