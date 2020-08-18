from os import chdir
from os.path import dirname, abspath
from sys import path

path.append('./src')

if __name__ == '__main__':
    chdir(dirname(abspath("__ file__")))

    from root import main

    main()
