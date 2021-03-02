# Contains helper functions for your apps!
from os import listdir, remove

# If the io following files are in the current directory, remove them!
# 1. 'currency_pair.txt'
# 2. 'currency_pair_history.csv'
# 3. 'trade_order.p'
import os
def check_for_and_del_io_files():
    # Your code goes here.
    filelist = os.listdir()
    for i in filelist:
        if i == 'currency_pair.txt':
            os.remove('currency_pair.txt')
        if i == 'currency_pair_history.csv':
            os.remove('currency_pair_history.csv')
        if i == 'trade_order.p':
            os.remove('trade_order.p')
    pass # nothing gets returned by this function, so end it with 'pass'.

#check_for_and_del_io_files()