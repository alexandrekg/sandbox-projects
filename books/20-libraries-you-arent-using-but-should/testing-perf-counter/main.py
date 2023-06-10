from time import perf_counter

n, m = map(int, [3, 5])
t1_start = perf_counter()

for i in range(n):
    t = int(input())
    if t % m == 0:
        print(t)

t1_stop = perf_counter()

print("Elapsed time:", t1_stop, t1_start)
print("Elapsed time during the whole program in seconds: ", t1_stop - t1_start)
