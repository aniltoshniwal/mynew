import os
import sys
print(os.getcwd()+"/"+sys.argv[0])
print(sys.argv[0])
print(os.path.dirname(os.path.realpath(__file__)))