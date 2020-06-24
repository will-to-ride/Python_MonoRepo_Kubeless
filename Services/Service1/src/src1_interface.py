import numpy as np

def interface(src1_input):

    array1 = 0
    array2 = 0

    try:
        array1 = src1_input['array_1']
    except:
        print("could not read array 1")

    try:
        array2 = src1_input['array_2']
    except:
        print("could not read array 2")

    new_array = add_arr(array1, array2)

    output_dic = {
        'newArray': new_array
    }

    return output_dic

def add_arr(num1, num2):
    return num1 + num2