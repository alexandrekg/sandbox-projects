import begin


@begin.start(auto_convert=True)
def main(a: 'First value' = 0.0, b: 'Second Value' = 0.0):
    """
        I'm not using if __name__ == "__main__": because begins is smart so,
        when we are using begin.start, this will be the starting point of the program

        Example:
            └> python begins_example.py -a 10 -b 15
                Result: 25.0
    """
    print(a + b)
