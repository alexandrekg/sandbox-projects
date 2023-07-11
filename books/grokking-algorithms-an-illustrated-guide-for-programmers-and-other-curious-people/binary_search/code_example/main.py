
def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) - 1
    
    mid = (low + high)
    guess = sorted_array[mid]
    if guess == item:
        return mid    
    if guess < item:
        low = mid + 1


if __name__ == "__main__":
    num_array = [1, 3, 5, 7, 9]
    print(binary_search(num_array, 3))
