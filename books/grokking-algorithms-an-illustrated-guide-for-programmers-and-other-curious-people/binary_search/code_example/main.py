
def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) - 1
    mid = round((low + high) / 2)
    guess = sorted_array[mid]
    total_guesses = 0
    
    if guess < item:
        low = mid + 1
        
    print('Total guesses: ', total_guesses)


if __name__ == "__main__":
    num_array = [i for i in range(101)]
    binary_search(num_array, 99)
