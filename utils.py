import numpy as np


def is_number(f):
    try:
        int(f)
        return True
    except:
        return False


def pd_convert_to_int(f):
    if not is_number(f):
        return -1
    else:
        return np.int32(int(f))
