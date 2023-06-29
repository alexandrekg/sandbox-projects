import psutil

cpu = psutil.cpu_percent(interval=5, percpu=True)

# it produces one value for each logical CPU
print(cpu)
