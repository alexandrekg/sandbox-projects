
def binary_search(sorted_array, item):
    low = 0
    high = len(list) - 1
    mid = (low + high) / 2
    guess = list[mid]
    total_guesses = 0
    
    if guess < item:
        low = mid + 1
        
    print('Total guesses: ', total_guesses)


if __name__ == "__main__":
    num_array = [i for i in range(101)]
    binary_search(num_array, 99)
