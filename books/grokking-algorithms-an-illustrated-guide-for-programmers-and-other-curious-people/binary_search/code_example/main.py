
def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) - 1
    total_guesses = 0
    right_guess = 0
    while low <= high:
        mid = round((low + high) / 2)
        guess = sorted_array[mid]
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1
        if guess == item:
            right_guess = guess
            break

        total_guesses += 1    
    print(f'Total guesses: {total_guesses}, guess number is: {right_guess}')


if __name__ == "__main__":
    num_array = [i for i in range(101)]
    binary_search(num_array, 99)
