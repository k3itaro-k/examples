'''
Binary search


'''
import random

def binary_search(data, target, start, end):
    if start > end:
        return False

    half =  (start + end) // 2

    if data[half] == target:
        return True
    elif data[half] > target:
        return binary_search(data, target, 0, half - 1)
    else:
        return binary_search(data, target, half + 1, end)


if __name__=="__main__":
    data = [random.randint(0,100) for i in range(0,10)]
    data.sort()
    print(data)
    target = int(input('what number would you like to find? '))
    found  = binary_search(data, target, 0, len(data))
    print(found)