"""
Implementation of the DELETE method for the z3nbox RESTful API.
"""


def deleteBox(event, context):
    """
    Delete z3nbox(es) configuration.
    """
    return {
        'message': 'Delete a z3nbox',
        'body': 'boxname'
    }
