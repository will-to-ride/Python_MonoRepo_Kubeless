import numpy as np

from Service1.src import add_arr

def multiply_arr(src2_input):

    array1 = np.zeros(2)
    array2 = np.zeros(2)

    number1 = 3
    number2 = 4

    try:
        array1 = np.asarray(src2_input['array_1'])
    except:
        print("could not read array 1")

    try:
        array2 = np.asarray(src2_input['array_2'])
    except:
        print("could not read array 2")

    new_array = np.multiply(array1, array2)

    output_dic = {
        'newArray': new_array.tolist()
    }

    add = add_arr(number1, number2)
    print(str(add))

    return output_dic