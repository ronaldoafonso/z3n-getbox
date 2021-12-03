"""
Implementation of the GET method for the z3nbox RESTful API.
"""

import boto3
import json


def getBox(event, context):
    """
    Get z3nbox(es) configuration.
    """
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('boxes')

    boxname = event.get('boxname')
    if boxname:
        box = table.get_item(Key={'boxname': boxname})
    else:
        box = {'message': 'No boxname provided.'}

    print(f'This is the box: {box}.')

    return {
        'message': 'Get a z3nbox',
        'body': json.dumps(box)
    }
