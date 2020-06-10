import numpy as np

def multiply_arr(src2_input):

    array1 = np.asarray(src2_input['array1'])
    array2 = np.asarray(src2_input['array2'])

    new_array = array1*array2

    output_dic = {
        'newArray': new_array
    }

    return output_dic