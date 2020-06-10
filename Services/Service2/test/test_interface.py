import unittest
import json
import numpy as np
import pandas as pd
import sys

sys.path.insert(1,'./src')

# import src1_interface
from handler import execute

true_array = np.array([1,2,3,4])

with open('./Services/Service2/test/test_input_2.json') as f:
    service2_input = json.load(f)


class TestService2(unittest.TestCase):

    def test_multiply(self):

        result = execute(service2_input)
        service2_output = json.loads(result)['body']
        
        check = pd.isnull(service2_output['newArray'])
        vnan = 'nan!'
        assert check is False, vnan

        if check is False:
            check2 = np.array_equal(service2_output['newArray'], true_array)
            check2_msg = 'true array: \n' + np.array2string(true_array) + '\n' + 'does not equal: \n' + np.array2string(service2_output['newArray'])
            
            assert check2 is True, check2_msg

suite = unittest.TestLoader().loadTestsFromTestCase(TestService2)
unittest.TextTestRunner(verbosity=2).run(suite)
