import os
from sys import path
path.append('./src')

if __name__ == '__main__':
    os.chdir(os.path.split(__file__)[0])

    from Root import main
    main()
