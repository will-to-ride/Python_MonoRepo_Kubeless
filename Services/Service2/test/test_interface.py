import unittest
import json
import numpy as np
import pandas as pd
import sys

sys.path.insert(1,'./src')
sys.path.insert(2,'../src')

# import src2_interface
from handler import execute

true_array = np.array([1, 4])

with open('./Services/Service2/test/test_input_2.json') as f:
    service2_input = json.load(f)


class TestService2(unittest.TestCase):

    def test_multiply(self):

        result = execute(service2_input, context=None)
        service2_output = json.loads(result)['body']
        service2_output_np = np.asarray(service2_output['newArray'])

        # check = np.isnan(service2_output_np).any()
        # vnan = 'nan!' + str(service2_output_np)
        # assert check is False, vnan
        
        # if check is False:
        check2 = np.array_equal(true_array, service2_output_np)
        check2_msg = 'true array: \n' + '2' + '\n' + 'does not equal: \n' + str(service2_output_np)
        
        assert check2 is True, check2_msg

suite = unittest.TestLoader().loadTestsFromTestCase(TestService2)
unittest.TextTestRunner(verbosity=2).run(suite)
