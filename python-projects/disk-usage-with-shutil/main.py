import shutil
import os


print(shutil.disk_usage(os.getcwd()))

"""
Return a tuple of total, used and free space data in bytes


(.venv) *[develop][~/workspace/sandbox-projects/python-projects]$ python disk-usage-with-shutil/main.py 
usage(total=982820896768, used=65871941632, free=866948870144)
"""