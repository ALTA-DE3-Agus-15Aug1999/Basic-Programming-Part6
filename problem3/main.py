def array_unique(arrayA, arrayB):
    unique_elements = []
    for element in arrayA:
        if element not in arrayB:
            unique_elements.append(element)
    # your code here
    return unique_elements

if __name__ == '__main__':
    print(array_unique([1, 2, 3, 4], [1, 3, 5, 10, 16])) # [2, 4]
    print(array_unique([10, 20, 30, 40], [5, 10, 15, 59])) # [20, 30, 40]
    print(array_unique([1, 3, 7], [1, 3, 5])) # [7]
    print(array_unique([3, 8], [2, 8])) # [3]
    print(array_unique([1, 2, 3], [3, 2, 1])) # []