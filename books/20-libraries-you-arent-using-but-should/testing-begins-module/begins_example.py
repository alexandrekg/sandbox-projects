import begin


@begin.start(auto_convert=True)
def main(a: 'First value' = 0.0, b: 'Second Value' = 0.0):
    print(a + b)