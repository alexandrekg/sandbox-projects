def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    
    while low <= high:
        mid = (low + high)
        guess = list(mid)
        
        if guess == item:
            return mid
        if guess > item:
            return mid - 1
        else:
            low = mid + 1

    return None

    
if __init__ == "__main__":
    binary_search()