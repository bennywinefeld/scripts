import sys, os

rootDir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(rootDir)

import jacob.my_module

jacob.my_module.testFunction()