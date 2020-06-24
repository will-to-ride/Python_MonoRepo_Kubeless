import sys
import json

from src.src1_interface import interface

def execute(event, context):
    
    data = event["data"]

    try:
        output = interface(data)
        response = {
            "statusCode": 200,
            "body": output
        }
        print(output)
    except:
        response = {
            "statusCode": 400,
            "body": data
        }
        print("Unexpected error:", sys.exc_info()[0])

    return json.dumps(response)