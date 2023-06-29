import psutil
import os, sys, time

pid = os.getpid()
p = psutil.Process(pid)
print('Process info:')
print('  name  :', p.name())
print('  exe   :', p.exe())

data = []
