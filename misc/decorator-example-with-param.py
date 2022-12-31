import torch
import torchvision
import torch.nn as nn
import code
from datetime import datetime

from functools import wraps

def print_fcn_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string, ": ", func.__name__, " entered...")
        result = func(*args, **kwargs)
        return result

    return wrapper

@print_fcn_name
def f1(p1):
    print("this is f1...")

f1(1)
