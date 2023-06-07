import sys


print(sys.base_prefix)


"""
[develop][~/workspace/sandbox-projects/python-projects/testing-sys-base-prefix]$ python printing-sys-base-prefix-without-virtualenv.py 
/home/alexkg/.pyenv/versions/3.10.9


(.venv) [develop][~/workspace/sandbox-projects/python-projects/testing-sys-base-prefix]$ python printing-sys-base-prefix-without-virtualenv.py  
/home/alexkg/.pyenv/versions/3.10.9


The output is the same because the virtualenv base Python installation is from pyenv, also the same interpreter I ran before
"""
