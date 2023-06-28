import begin


@begin.start(auto_convert=True)
def main(a: 'First value' = 0.0, b: 'Second Value' = 0.0):
    """
        I'm not using if __name__ == "__main__": because begins is smart so,
        when we are using begin.start, this will be the starting point of the program
    """
    print(a + b)
