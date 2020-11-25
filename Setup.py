import os

try:
    os.system('pip install art')
    os.system('pip install mss')
    os.system('pip install pygame')
except:
    print('Script Failed, maybe you would like to install the libraries yourself?')
    print('list of needed modules:')
    print('art')
    print('mss')
    print('pygame')