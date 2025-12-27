# OPTION 1: import the entire math module
import math
print(math.sqrt(16))

# OPTION 2: import only the sqrt function from module
from math import sqrt
print(sqrt(16))

# OPTION 3: import method with an alias
from math import sqrt as s
print(s(25))

# OPTION 4: import the entire module with an alias
# NOTE: not recommended, can import same name methods
from math import *
print(sqrt(49))
