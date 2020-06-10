import sys
import json

from src1_interface import add_arr

def execute(event, context):
    
    data = event["data"]

    try:
        output = add_arr(data)
        response = {
            "statusCode": 200,
            "body": output
        }
        print(output)
    except:
        print("Unexpected error:", sys.exc_info()[0])

    return json.dumps(response)