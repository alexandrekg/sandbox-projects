
def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) - 1
    
    while low <= high:    
        mid = round((low + high) / 2)
        guess = sorted_array[mid]
        if guess < item:
            low = mid + 1
            print(low)
        if guess > item:
            high = mid - 1
            print(high)
        if guess == item:
            return mid    
        else:
            return None


if __name__ == "__main__":
    num_array = [1, 3, 5, 7, 9]
    print(binary_search(num_array, 3))
