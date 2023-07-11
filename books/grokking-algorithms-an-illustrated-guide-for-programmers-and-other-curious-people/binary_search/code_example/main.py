
def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) - 1
    mid = round((low + high) / 2)
    guess = sorted_array[mid]
    total_guesses = 0
    
    if guess < item:
        low = mid + 1


if __name__ == "__main__":
    num_array = [1, 3, 5, 7, 9]
    print(binary_search(num_array, 3))
