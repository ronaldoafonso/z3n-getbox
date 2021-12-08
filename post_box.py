"""
Implementation of the POST method for the z3nbox RESTful API.
"""


def postBox(event, context):
    """
    Post z3nbox(es) configuration.
    """
    return {
        'message': 'Post a z3nbox',
        'body': 'boxname'
    }
