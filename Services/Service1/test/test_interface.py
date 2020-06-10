import unittest
import json
import numpy as np
import pandas as pd
import sys

sys.path.insert(1,'./src')

# import src1_interface
from handler import execute

true_array = np.array([2,4,6,8])

with open('./Services/Service1/test/test_input_1.json') as f:
    service1_input = json.load(f)


class TestService1(unittest.TestCase):

    def test_ass(self):

        result = execute(service1_input)
        service1_output = json.loads(result)['body']
        
        check = pd.isnull(service1_output['newArray'])
        vnan = 'nan!'
        assert check is False, vnan

        if check is False:
            check1 = np.array_equal(service1_output['newArray'], true_array)
            check1_msg = 'true array: \n' + np.array2string(true_array) + '\n' + 'does not equal: \n' + np.array2string(service1_output['newArray'])
            
            assert check1 is True, check1_msg

suite = unittest.TestLoader().loadTestsFromTestCase(TestService1)
unittest.TextTestRunner(verbosity=2).run(suite)
