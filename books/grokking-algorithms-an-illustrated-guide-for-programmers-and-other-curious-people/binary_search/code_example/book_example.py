def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    
    while low <= high:
        mid = (low + high)
        guess = my_list[mid]
        
        if guess == item:
            return mid
        if guess > item:
            return mid - 1
        else:
            low = mid + 1

    return None

    
if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))