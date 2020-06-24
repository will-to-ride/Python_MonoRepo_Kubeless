import unittest
import json
import numpy as np
import pandas as pd
import sys

sys.path.insert(1,'./src')
sys.path.insert(2,'../src')

# import src1_interface
from handler import execute

true_array = 3

with open('./Services/Service1/test/test_input_1.json') as f:
    service1_input = json.load(f)


class TestService1(unittest.TestCase):

    def test_add(self):

        result = execute(service1_input, context=None)
        service1_output = json.loads(result)['body']
        service1_output_np = service1_output['newArray']

        check = pd.isnull(service1_output_np)
        vnan = 'nan!' + str(service1_input)
        assert check is False, vnan

        if check is False:
            check1 = (service1_output_np == true_array)
            check1_msg = 'true array: \n' + '2' + '\n' + 'does not equal: \n' + str(service1_output_np)
            
            assert check1 is True, check1_msg

suite = unittest.TestLoader().loadTestsFromTestCase(TestService1)
unittest.TextTestRunner(verbosity=2).run(suite)
