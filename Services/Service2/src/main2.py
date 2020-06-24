from __future__ import print_function

import pprint
import sys
import numpy

from src.src2_interface import multiply_arr

def main():

    thisdict = {
                "array_1": [1,2],
                "array_2": [1,2]
                }

    new_dict = multiply_arr(thisdict)
    print(new_dict)


if __name__ == "__main__":
    sys.exit(main())
