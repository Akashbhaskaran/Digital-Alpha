# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:28:08 2018

@author: user
"""

import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print(password)