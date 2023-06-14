# Code Example

This example was made by ChatGPT for me to understand the concepts of contextmanager, with an example with/without using contextmanager

About the example with context manager (explanation):
- Inside the timing function, t0 start the timer;
- The `yield` statement jumps off the timing function and get back to execute my_function;
- When `my_function` ends, the runs the remaining timing() function, starting with t1 ending timer and then prints the execution time