import sys
import json

from Service2.src import multiply_arr

def execute(event, context):
    
    data = event["data"]

    try:
        output = multiply_arr(data)
        response = {
            "statusCode": 200,
            "body": output
        }
        print(output)
    except:
        response = {
            "statusCode": 400,
            "body": "oops"
        }
        print("Unexpected error:", sys.exc_info()[0])

    return json.dumps(response)